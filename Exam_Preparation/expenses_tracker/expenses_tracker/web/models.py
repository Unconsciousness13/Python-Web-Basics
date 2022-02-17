from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import validate_only_letters, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TI_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TI_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )


class Expense(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    price = models.FloatField()

    image = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )
