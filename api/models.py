from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="""Ім'я Доктора""")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    direction = models.ManyToManyField(Direction, verbose_name='Напрямок', related_name='direction')
    description = models.CharField(max_length=300, verbose_name='Опис')
    birthday = models.DateField(verbose_name='День народження')
    work_experience = models.IntegerField(verbose_name='Досвід роботи')

