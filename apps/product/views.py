from django.shortcuts import render

from django.views.generic import ListView
from .models import Food

# Create your views here.


class ProductListView(ListView):
    model = Food
    template_name = 'page/product_list.html'
    context_object_name = 'products'
    queryset = Food.objects.all()








