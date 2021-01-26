#blank = true не обязвтельное поле для заполнения


python manage.py shell

#проверка запроса к базе данных
from django.db import connection
connection.queries

from shop.models import Category
Category(title='Шорты', slug='shorts')
category1 = _
category1.save()
Category(title='Майки', slug='t-shorts')
category2 = _
category2.save()
category3 = Category.objects.create(title='Тапки', slug='slippers')
category4 = Category.objects.create(title='Кепки', slug='caps')
Category.objects.all()


from shop.models import Tags
tags1 = Tags.objects.create(title='Распродажа', slug='sale')
tags2 = Tags.objects.create(title='Новинки', slug='new')
Tags.objects.filter(title='Распродажа')
Tags.objects.order_by('title')

from shop.models import Seller
seller1 = Seller.objects.create(name='Иван', description='Обо мне я Иван')
seller2 = Seller.objects.create(name='Мария', description='Обо мне я Мария')

from shop.models import Product
product1 = Product.objects.create(title='Майка первая', slug='mayka-pervaya', description='Коллаборация Billabong x Metallica - это часть проекта Billabong LAB')
product2 = Product.objects.create(title='Майка вторая', slug='mayka-vtoraya', description='Специально для больших фанатов Star Wars компания Levis')
