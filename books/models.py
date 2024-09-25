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
                             verbose_name='Enter a book`s title', db_index=True, null=True)
    author = models.CharField(max_length=250,
                              verbose_name='Enter the book`s author', db_index=True, null=True)
    genre = models.CharField(max_length=200, choices=GENRE, db_index=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Enter the book`s price', db_index=True, null=True)
    created_at = models.DateField(verbose_name='Enter the year of publication', db_index=True, null=True)
    pages = models.PositiveIntegerField(verbose_name='Enter the number of pages', db_index=True, null=True)
    cover = models.ImageField(upload_to='book/',
                              verbose_name='Download the book`s cover', db_index=True, null=True)
    description = models.TextField(verbose_name='Add the book`s description', db_index=True, null=True)
    publisher_url = models.URLField(verbose_name='Enter the publisher`s webiste address', db_index=True, null=True)
    publisher_email = models.EmailField(verbose_name='Enter the publisher`s email address', db_index=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


class Review(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review', db_index=True, null=True)
    review_text = models.TextField(db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.book_name} - {self.created_at}'