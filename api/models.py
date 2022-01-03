from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie2rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2rating")
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

    def __str__(self):
        return self.movie

