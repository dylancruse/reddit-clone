from django.urls import path

from redditclone import views

urlpatterns = [
        path('', views.index, name='index'),
        path('detail', views.detail, name='detail'),
        path('create', views.create, name='create')
    ]