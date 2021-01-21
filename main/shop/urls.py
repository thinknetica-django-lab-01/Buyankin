from django.urls import path
from .views import *
from django.contrib.flatpages import views

urlpatterns = [
    path('', index, name='index'),
    path('<path:url>', views.flatpage),
]