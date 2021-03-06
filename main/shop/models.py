from django.db import models
from django.urls import reverse

# Create your models here.

'''
Category
--------
title 
slug

Tags
-------
title 
slug

Seller
-------
name
description
address
bought

Product
-------
title 
slug
description
specifications
photo
views
sell
category
tags

'''

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name = 'Наименование категории')
    slug = models.SlugField(max_length=255, unique=True, verbose_name = 'URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['title']

class Tags(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название тега')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'
        ordering = ['title']

class Seller(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя продавца')
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    bought = models.IntegerField(default=0, verbose_name='Кол-во покупок')
    date_of_birth = models.DateField(null=True, blank=True)
    e_mail = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile_update', kwargs={'pk': self.pk})

class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    sell = models.IntegerField(default=0, verbose_name='Кол-во продаж')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='products')
    tags = models.ManyToManyField(Tags, related_name='tags')
    price = models.IntegerField(default=0, blank=False, verbose_name='Стоимость')

    def __str__(self):
        return self.title