from django.contrib import admin
from .models import Category

@admin.register(Category)
class LemonsAdmin(admin.ModelAdmin):
    list_display = ['title','text','img','price','slug',]
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
