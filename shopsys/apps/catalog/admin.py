from django.contrib import admin
from .models import Category, Product
from .forms import ProductAdminForm
# Register your models here.


@admin.register(Product)  # 管理Product类
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_per_page = 50  # 一页50条
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at')  # 不需要手动添加的属性
    prepopulated_fields = {'slug': ('name',)}  # 自动填充,填写name,slug自动填写


@admin.register(Category)  # 管理Category类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}



