# Generated by Django 3.1.5 on 2021-01-26 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True)),
                ('specifications', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('sell', models.IntegerField(default=0, verbose_name='Кол-во продаж')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя продавца')),
                ('description', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('bought', models.IntegerField(default=0, verbose_name='Кол-во покупок')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['title'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Тег'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tags',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=255, verbose_name='Наименование категории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.SlugField(default=' ', unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Название тега'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='shop.Tags'),
        ),
    ]
