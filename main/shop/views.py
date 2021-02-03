from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Seller, Tags


class IndexView(TemplateView):
    model = Product
    paginate_by = 10
    context_object_name = 'product'
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()[:5]
        return context


class GoodsList(ListView):
    model = Product
    paginate_by = 10
    template_name = 'shop/goods.html'
    tags = Tags.objects.all()

    def get_queryset(self, **kwargs):
        tag = self.request.GET.get('tag')
        if tag:
            return Product.objects.filter(tags__title=tag)
        return super().get_queryset(**kwargs)

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