from django.db import models


class NewsModel(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    type = models.ForeignKey(to='TypeNewsModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TypeNewsModel(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
