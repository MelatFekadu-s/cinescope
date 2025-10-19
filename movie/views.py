from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-created_at')
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

