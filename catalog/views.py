from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product, Contacts, Article
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index_home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


def index_contacts(request):
    if request.method == "POST":
        first_name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contacts(first_name=first_name, phone=phone, message=message)
        contact.save()
        with open('data.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{first_name} ({phone}): {message}'+'\n')
    contacts = Contacts.objects.all()

    return render(request, 'catalog/index_contacts.html', {'contacts': contacts})


def contact_list(request):
    Contacts.objects.all()

class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('catalog:index_home')
