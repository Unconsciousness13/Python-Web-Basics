from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN)
    image_url = models.URLField(max_length=300)


class Book(models.Model):
    TITLE_MAX_LENGTH = 30

    TYPE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)

    description = models.TextField()
    image = models.URLField(max_length=300)
    type = models.CharField(max_length=TYPE_MAX_LENGTH)
