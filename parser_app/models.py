from django.db import models


class ParserRezka(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='parser/')

    def __str__(self):
        return self.title
