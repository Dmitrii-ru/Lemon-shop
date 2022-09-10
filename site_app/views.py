from django.shortcuts import render
from django.views.generic import ListView

from .models import Category



class CatalogLemon(ListView):
    template_name = 'site_app/category.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'Category'

def index(request):
    return render(request, 'site_app/index.html')


def catalog(request):
    return render(request, 'site_app/category.html')


def contacts(request):
    return render(request, 'site_app/contacts.html')
