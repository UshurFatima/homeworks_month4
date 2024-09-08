from django.db import models


class Book(models.Model):
    GENRE = (
        ('fantasy', 'fantasy'),
        ('sci-fi', 'sci-fi'),
        ('horror', 'horror'),
        ('thriller', 'thriller'),
        ('detective', 'detective'),
        ('romance', 'romance'),
        ('classics', 'classics'),
        ('philosophy', 'philosophy'),
        ('history', 'history'),
        ('religion', 'religion'),
    )
    title = models.CharField(max_length=250,
                             verbose_name='Enter a book`s title')
    author = models.CharField(max_length=250,
                              verbose_name='Enter the book`s author')
    genre = models.CharField(max_length=200, choices=GENRE, null=True)
    price = models.PositiveIntegerField(verbose_name='Enter the book`s price')
    created_at = models.DateField(verbose_name='Enter the year of publication')
    pages = models.PositiveIntegerField(verbose_name='Enter the number of pages')
    cover = models.ImageField(upload_to='book/',
                              verbose_name='Download the book`s cover')
    desciption = models.TextField(verbose_name='Add the book`s description', null=True)
    publisher_url = models.URLField(verbose_name='Enter the publisher`s webiste address')
    publisher_email = models.EmailField(verbose_name='Enter the publisher`s email address')

    def __str__(self):
        return f'{self.title} - {self.author}'
