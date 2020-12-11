from django.contrib import admin
from .models import Book, Home, Category, Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Home)
admin.site.register(Category)
admin.site.register(Tag)