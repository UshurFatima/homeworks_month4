from django.db import models
import employees.models


class Movie(models.Model):
    MOVIE_GENRE = (
        ('thriller', 'thriller'),
        ('romance', 'romance'),
        ('detective', 'detective'),
        ('fantasy', 'fantasy'),
        ('comedy', 'comedy'),
        ('history', 'history'),
        ('action', 'action'),
    )

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='movies/')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    genre = models.CharField(max_length=100, choices=MOVIE_GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.genre}'


class Review(models.Model):
    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    user = models.ForeignKey(employees.models.User, on_delete=models.CASCADE, related_name='user')
    comment = models.TextField()
    rating = models.PositiveIntegerField(choices=RATING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'