from django.urls import path
from catalog.views import (index_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, VersionCreateView, VersionUpdateView, VersionListView)
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', index_contacts, name="index_contacts"),
    path('', ProductListView.as_view(), name="index_home"),
    path('<int:pk>/catalog/', ProductDetailView.as_view(), name="product"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="update_product"),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name="delete_product"),
    path('versions/create_version/', VersionCreateView.as_view(), name="create_version"),
    path('versions/update_version/<int:pk>', VersionUpdateView.as_view(), name="update_version"),
    path('versions/', VersionListView.as_view(), name="version_list"),


]
