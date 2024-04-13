from django.urls import path
from catalog.views import index_contacts, contact_list, ProductListView, ProductDetailView, ArticleCreateView
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', index_contacts, name="index_contacts"),
    path('', ProductListView.as_view(), name="index_home"),
    path('<int:pk>/catalog/', ProductDetailView.as_view(), name="product"),
    path('contacts_list/', contact_list, name="contact_list"),
    path('articles/create/', ArticleCreateView.as_view(), name="create_article"),
    #path('articles/', ArticleListView.as_view(), name="articles"),

]
