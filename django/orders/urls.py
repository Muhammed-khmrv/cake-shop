from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('my-orders/', views.order_list, name='order_list'),
]