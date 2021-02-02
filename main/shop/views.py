from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator

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
    paginate_by = 10
    template_name = 'shop/goods.html'
    tags = Tags.objects.all()

    # def get_queryset(self, **kwargs):
    #     tag = self.request.GET.get('tag')
    #     if tag:
    #         return Product.objects.filter(tag_product__title_tag=tag)
    #     return super().get_queryset(**kwargs)
    #
    # def context_data(self, **kwargs):
    #     context = super(self).get_context_data(**kwargs)
    #     my_tag = self.request.GET.get('tag')
    #     if my_tag:
    #         context['tag'] = my_tag
    #     return context

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tags'] = Tags.objects.all()
        return data


class GoodsDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/goods_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GoodsDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['tags_list'] = Tags.objects.all()
        return context