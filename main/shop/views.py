from django.shortcuts import render

from .models import Product

def index(request):
    product = Product.objects.all()
    context = {
        'product': product,
        'title': 'Список'
    }
    return render(request, 'shop/index.html', context=context)