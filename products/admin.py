from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'description',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
