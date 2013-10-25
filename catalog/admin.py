# coding: utf-8
from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'published', 'ordering', 'pic')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(ProductImages)