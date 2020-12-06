from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('search', views.SearchView.as_view(), name='search'),
]