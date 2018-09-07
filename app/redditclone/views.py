from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'index.html', {
        'posts': posts
    })

def detail(request):
    return render(request, 'detail.html')

def create(request):
    return render(request, 'create.html')