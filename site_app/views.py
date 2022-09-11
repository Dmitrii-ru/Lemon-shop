from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category


class CatalogLemon(ListView):
    template_name = 'site_app/category.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'Category'


def detail_pro(request, slug):
    product = get_object_or_404(Category, slug=slug)

    context = {'product': product}
    return render(request, 'site_app/detail_pro.html', context=context)


def index(request):
    return render(request, 'site_app/index.html')


def catalog(request):
    return render(request, 'site_app/category.html')


def contacts(request):
    return render(request, 'site_app/contacts.html')
