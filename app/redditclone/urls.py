from django.urls import path

from redditclone import views

urlpatterns = [
        path('', views.index, name='index')
    ]