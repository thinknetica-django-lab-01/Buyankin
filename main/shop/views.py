from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Seller, Tags
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UpdateProfile, UpdateGoods
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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


class ProfileCreate(CreateView):
    model = Seller
    fields = '__all__'


class ProfileUpdate(UpdateView):
    model = Seller
    success_url = '/'
    template_name = 'shop/seller_form.html'
    form_class = UpdateProfile

    def get_object(self):
        return self.request.user


class ProfileDelete(DeleteView):
    model = Seller
    success_url = reverse_lazy('seller')


class GoodsCreate(CreateView):
    model = Product
    form_class = UpdateGoods
    permission_required = ("main.add_goods", "main.change_goods")

    def form_valid(self, form):
        messages.success(self.request, "Сохранено")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Сохранение не удалось!")
        return super().form_invalid(form)


class GoodsUpdate(UpdateView):
    model = Product
    success_url = '/'
    template_name = 'shop/product_form.html'
    form_class = UpdateGoods
    permission_required = ("main.add_goods", "main.change_goods")

    def form_valid(self, form):
        messages.success(self.request, "Сохранено")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Сохранение не удалось!")
        return super().form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def user_login(request):
    return render(request, 'shop/login.html')