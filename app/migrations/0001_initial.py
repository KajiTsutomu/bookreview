# Generated by Django 3.0.8 on 2020-11-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('author', models.CharField(max_length=20, verbose_name='著者')),
                ('publish', models.CharField(max_length=20, verbose_name='出版社')),
                ('publish_date', models.DateField(verbose_name='出版日')),
                ('outline', models.TextField(verbose_name='概要')),
                ('impression', models.TextField(verbose_name='感想')),
                ('image', models.ImageField(upload_to='bookimage', verbose_name='本の表紙')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='トップページのタイトル')),
                ('topimage', models.ImageField(upload_to='topimage', verbose_name='トップ画像')),
            ],
        ),
    ]
