from django.urls import path
from . import views

urlpatterns = [
    path('', views.cake_list, name='cake_list'),
    path('category/<slug:slug>', views.cakes_by_category, name='cakes_by_category'),
    path('<slug:slug>', views.cake_detail, name='cake_detail'),
]