from django.urls import path


urlpatterns = [
    path('', views.main_page, name='main_page'),
]
