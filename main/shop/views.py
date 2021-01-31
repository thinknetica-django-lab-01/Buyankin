from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Product, Seller, Tags

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

class GoodsList(ListView):
    model = Product
    template_name = 'shop/goods.html'

class GoodsDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/goods_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GoodsDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tags_list'] = Tags.objects.all()
        return context