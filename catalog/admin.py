from django.contrib import admin
from catalog.models import Product, Category, Contacts, Version
from article.models import Article


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'is_activegi')
    list_filter = ('number', 'name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'email',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'content',)
