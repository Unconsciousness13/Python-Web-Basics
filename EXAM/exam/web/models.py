from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

from exam.web.validators import validate_only_letters_nums_underscore


class Profile(models.Model):
    USERNAME_MAX_LEN = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(2),
            validate_only_letters_nums_underscore,
        )

    )

    email = models.EmailField(

    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )


class Album(models.Model):
    ALBUM_MAX_CHARS = 30

    album_name = models.CharField(
        max_length=ALBUM_MAX_CHARS,
        unique=True
    )

    artist = models.CharField(max_length=ALBUM_MAX_CHARS)

    genre = models.CharField(
        max_length=ALBUM_MAX_CHARS,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R&B Music', 'R&B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other'),
        )

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    img_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )
    )
