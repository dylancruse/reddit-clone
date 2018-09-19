from django.urls import path

from redditclone import views, drf_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', drf_views.PostModelViewSet, base_name='post')

urlpatterns = [
        path('', views.index, name='index'),
        path('detail', views.detail, name='detail'),
        path('create', views.create, name='create')
    ]

urlpatterns += router.urls