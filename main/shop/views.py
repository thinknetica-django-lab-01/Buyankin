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

    # def listing(request):
    #     contact_list = Product.objects.all()
    #     paginator = Paginator(contact_list, 10)  # Show 10 goods per page.
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'shop/goods.html', {'page_obj': page_obj})

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