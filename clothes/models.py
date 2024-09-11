from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name