from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth import get_user_model


User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username

    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'title', 'body', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'created_at', 'reviews']
