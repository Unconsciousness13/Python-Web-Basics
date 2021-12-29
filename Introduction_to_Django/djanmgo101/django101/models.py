from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    home_town = models.CharField(default='Sofia', max_length=25)