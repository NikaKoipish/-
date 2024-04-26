from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index_home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.name = active_versions.last().name
                product.number = active_versions.last().number
        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index_home')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index_home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index_home')


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
