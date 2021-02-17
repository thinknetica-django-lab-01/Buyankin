from django.urls import path, include
from .views import *
from django.contrib.flatpages import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('goods/', GoodsList.as_view(), name='goods'),
    path('goods/<int:pk>/', GoodsDetail.as_view(), name='goods-detail'),
    path('pages/about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('pages/product/', views.flatpage, {'url': '/product/'}, name='product'),
    path('pages/contact/', views.flatpage, {'url': '/contact/'}, name='contact'),
    path('accounts/profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('accounts/profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('accounts/profile/<int:pk>/delete/', ProfileDelete.as_view(), name='profile_delete'),
    path('goods/add', GoodsCreate.as_view(), name='goods_create'),
    path('goods/<int:pk>/edit/', GoodsUpdate.as_view(), name='goods_update'),

    path('accounts/', include('allauth.urls')),
]