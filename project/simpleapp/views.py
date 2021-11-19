from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'
    context_object_name = 'products'
