from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.db.models import Avg


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def str(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in minutes")
    director = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    poster_url = models.URLField(blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    def str(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1–5
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_reviews", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("movie", "user")

    @property
    def likes_count(self):
        return self.liked_by.count()

    def str(self):
        return f"{self.movie} - {self.rating}⭐️ by {self.user}"