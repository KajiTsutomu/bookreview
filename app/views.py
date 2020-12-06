from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View
from .models import Book, Home, Category, Profile
from django.db.models import Q

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        home_data = Home.objects.all()
        book_data = Book.objects.all()

        if book_data.exists():
            book_data = book_data.order_by('-id')

        paginator = Paginator(book_data, 10)
        page = request.GET.get('page')
        book_data = paginator.get_page(page)

        return render(request, 'app/index.html', {
            'home_data' : home_data,
            'book_data' : book_data
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):
        book_data = Book.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'book_data' : book_data
        })

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_data = Category.objects.get(name=self.kwargs['category'])
        book_data = Book.objects.order_by('-id').filter(category=category_data)

        paginator = Paginator(book_data, 10)
        page = request.GET.get('page')
        book_data = paginator.get_page(page)

        return render(request, 'app/index.html', {
            'book_data' : book_data
        })

class SearchView(View):
    def get(self, request, *args, **kwargs):
        book_data = Book.objects.all().order_by('-id')
        keyword = self.request.GET.get('keyword')

        if keyword:
            book_data = book_data.filter(
                Q(title__icontains=keyword) | Q(author__icontains=keyword) | Q(publish__icontains=keyword) | Q(category__name__icontains=keyword)
            )

        paginator = Paginator(book_data, 10)
        page = request.GET.get('page')
        book_data = paginator.get_page(page)
        
        return render(request, 'app/index.html', {
            'keyword' : keyword,
            'book_data' : book_data
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        return render(request, 'app/about.html', {
            'profile_data' : profile_data
        })