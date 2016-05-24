from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)


class Sheet(models.Model):
    name = models.CharField(max_length=100)
    books = models.ForeignKey(Book, related_name='sheets')
    page = models.OneToOneField('Page')


class Page(models.Model):
    name = models.CharField(max_length=100)
