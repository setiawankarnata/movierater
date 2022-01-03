from django.shortcuts import render
from .models import Movie, Rating
from rest_framework import viewsets
from .serializers import MovieSerializers, RatingSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
