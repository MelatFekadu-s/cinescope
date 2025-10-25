from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Review, Genre

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    liked_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'movie', 'user', 'rating', 'title', 'body',
            'likes_count', 'liked_by', 'created_at', 'updated_at',
        ]
        read_only_fields = ['user', 'created_at', 'updated_at', 'likes_count', 'liked_by']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    review_count = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'slug', 'description', 'genres', 'release_date',
            'duration', 'director', 'language', 'country', 'poster_url',
            'average_rating', 'review_count', 'created_at', 'reviews',
        ]

    def get_review_count(self, obj):
        return obj.reviews.count()


class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False
    )

    class Meta:
        model = Movie
        fields = [
            'title', 'description', 'release_date', 'duration',
            'director', 'language', 'country', 'poster_url', 'genres',
        ]