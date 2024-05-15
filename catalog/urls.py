from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (index_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, CategoryListView)
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', index_contacts, name="index_contacts"),
    path('', ProductListView.as_view(), name="index_home"),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="product"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="update_product"),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name="delete_product"),
    path('category_list/', CategoryListView.as_view(), name="category_list"),

]
