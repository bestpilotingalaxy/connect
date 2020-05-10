from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdvertList.as_view(), name='main'),
    path('<str:platform_name>/', views.by_platform, name='by_platform'),
    path('add/', views.add_and_save, name='add'),
]
