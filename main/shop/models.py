from django.db import models

# Create your models here.
# товар, категория, тэги, продавец
# product category tags seller




class Shop(models.Model):
    product = models.CharField(max_length=100, verbose_name = 'Навание товара')
    seller = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    tags = models.ForeignKey('Tags', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product

class Category(models.Model):
    category = models.CharField(max_length=150, db_index=True, verbose_name = 'Наименование категории')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['category']

class Tags(models.Model):
    tags = models.CharField(max_length=150, db_index=True, verbose_name = 'Теги')

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
        ordering = ['tags']