# Generated by Django 4.0.2 on 2022-02-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.URLField(max_length=300),
        ),
    ]