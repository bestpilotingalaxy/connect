from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.AdvertList.as_view(), name='main'),

    path('filter/',
         views.FilterAdvertsView.as_view(), name='filter'),

    path('search/',
         views.Search.as_view(), name='search'),

    path('review/<int:pk>/',
         views.AddReview.as_view(), name='add_review'),

    path('<str:platform_name>/',
         views.AdvertByPlatformView.as_view(), name='by_platform'),

    path('add/form/',
         views.AdvertAddView.as_view(), name='add'),

    path('detail/<int:pk>/',
         views.AdvertDetailView.as_view(), name='detail'),

    path('update/<int:pk>/',
         views.AdvertUpdateView.as_view(), name='update'),
]
