from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/<slug:category>/<slug:product>/',
         views.info_product, name='info_product'),
    path('products/', views.list_categories, name='list_categories'),
    path('products/<slug:category>/',
         views.category_products, name='category_products'),
]
