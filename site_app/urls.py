from django.urls import path
from . import views
from .views import CatalogLemon


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', CatalogLemon.as_view(), name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
]
