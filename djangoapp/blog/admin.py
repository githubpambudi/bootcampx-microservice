from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, News


admin.site.register(Category)
admin.site.register(News)