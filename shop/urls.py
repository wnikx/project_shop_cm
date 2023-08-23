from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/', views.list_categories, name='list_categories'),
    path('products/<slug:category>/',
         views.category_products, name='category_products'),
]
