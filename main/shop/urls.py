from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('pages/', index, name='index'),
    path('pages/about/', about, name='about'),
    path('pages/contact/', contact, name='contact'),
]