from django.urls import path
from catalog.views import index_home, index_contacts, product
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', index_contacts, name="index_contacts"),
    path('', index_home,name="index_home"),
    path('<int:pk>/catalog/', product, name="product")
]
