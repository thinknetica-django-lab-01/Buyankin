#blank = true не обязвтельное поле для заполнения


python manage.py shell

from shop.models import Shop
Shop(product='майка', seller='Иван')
product1 = _
product1.save()
product1.id

#второй вариант
product2 = Shop()
product2.product = 'кофта'
product2.seller = 'Маша'
product2.save()

#третий вариант
product2 = Shop.objects.create(product='кофта', seller='Маша')
product2.pk

#проверка запроса к базе данных
from django.db import connection
connection.queries
