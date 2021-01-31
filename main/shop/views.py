from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, Seller

def index(request):
    product = Product.objects.all()
    turn_on_block = True
    name_seller = Seller.objects.get(name='Иван').name
    context = {
        'product': product,
        'title': 'Список',
        'turn_on_block': turn_on_block,
        'name_seller': name_seller,
        'hi_world': 'Привет Мир!'
    }
    return render(request, 'shop/index.html', context=context)
#
# def goods(request):
#     product = Product.objects.all()
#     context = {
#         'product': product,
#         'title': 'Список всех товаров'
#     }
#     return render(request, 'shop/goods.html', context=context)

class GoodsList(ListView):
    model = Product
    template_name = 'shop/goods.html'