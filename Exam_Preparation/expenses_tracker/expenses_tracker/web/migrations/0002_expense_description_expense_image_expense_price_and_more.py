# Generated by Django 4.0.2 on 2022-02-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
