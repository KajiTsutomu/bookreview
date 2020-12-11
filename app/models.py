from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField('カテゴリ', max_length = 100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('タイトル', max_length = 100)
    category = models.ForeignKey(Category, verbose_name = 'カテゴリ', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
    author = models.CharField('著者', max_length = 20)
    publish = models.CharField('出版社', max_length = 20)
    publish_date = models.DateField('出版日')
    outline = models.TextField('概要')
    impression = models.TextField('感想')
    image = models.ImageField(upload_to='bookimage', verbose_name='本の表紙')
    created_date = models.DateField('作成日', default=timezone.now)
    evaluation = models.IntegerField('評価')
    amazon = models.CharField('amazon', max_length = 200, null = True, blank = True)
    rakuten = models.CharField('rakuten', max_length = 200, null = True, blank = True)

    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField('トップページのタイトル', max_length = 100)
    topimage = models.ImageField(upload_to = 'topimage', verbose_name='トップ画像')

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField('名前', max_length = 20)
    profile = models.TextField('プロフィール')
    mail = models.CharField('e-mail', max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.name