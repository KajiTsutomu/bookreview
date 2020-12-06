from django.contrib import admin
from .models import Book, Home, Category

# Register your models here.
admin.site.register(Book)
admin.site.register(Home)
admin.site.register(Category)