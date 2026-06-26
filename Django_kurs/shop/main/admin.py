from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Поля, которые будут заполнены автоматически

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display =['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category'] # фильтрация
    list_editable = ['price', 'available'] # изменения
    prepopulated_fields = {'slug': ('name',)}