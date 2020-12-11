from .models import Category, Tag
from django.db.models import Count

def common(request):
    category_data = Category.objects.all()
    tag_data = Tag.objects.all()
    context = {
        'category_data':category_data,
        'tag_data':tag_data,
    }
    return context