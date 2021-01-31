from django.urls import path
from .views import *
from django.contrib.flatpages import views

urlpatterns = [
    path('', index, name='index'),
    path('goods/', GoodsList.as_view(), name='goods'),
    path('<path:url>', views.flatpage),
    path('pages/about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('pages/product/', views.flatpage, {'url': '/product/'}, name='product'),
    path('pages/contact/', views.flatpage, {'url': '/contact/'}, name='contact'),

]