# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='名称', max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', help_text='根据name生成，用于生成页面URL,必须唯一')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(verbose_name='是否激活', default=True)),
                ('meta_keywords', models.CharField(verbose_name='Meta 关键词', max_length=225, help_text='meta关键词，有利于SEO,用逗号分隔')),
                ('meta_description', models.CharField(verbose_name='Meta描述', max_length=255, help_text='meta描述')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'db_table': 'categories',
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='名称', max_length=225)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', max_length=255, help_text='根据name生成的，用于生成页面URL, 必须唯一')),
                ('brand', models.CharField(verbose_name='品牌', max_length=50)),
                ('sku', models.CharField(verbose_name='计量单位', max_length=50)),
                ('price', models.DecimalField(max_digits=60, verbose_name='价格', decimal_places=2)),
                ('old_price', models.DecimalField(blank=True, max_digits=60, verbose_name='原来价格', decimal_places=2, default=0.0)),
                ('image', models.ImageField(verbose_name='图片', max_length=50, upload_to='')),
                ('is_active', models.BooleanField(verbose_name='设为激活', default=True)),
                ('is_featured', models.BooleanField(verbose_name='标为畅销', default=False)),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(verbose_name='Meta关键词', max_length=255, help_text='meta关键词标签,逗号分隔')),
                ('meta_description', models.CharField(verbose_name='Meta描述', max_length=255, help_text='meta描述标签')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
