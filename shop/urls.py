from django.urls import path


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<category>/', views.list_categories, name='list_categories'),
]
