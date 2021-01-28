from django.shortcuts import render

from .models import Product, Seller

def index(request):
    product = Product.objects.all()
    turn_on_block = True
    name_seller = Seller.objects.get(name='Иван').name
    context = {
        'product': product,
        'title': 'Список',
        'turn_on_block': turn_on_block,
        'name_seller': name_seller
    }
    return render(request, 'shop/index.html', context=context)