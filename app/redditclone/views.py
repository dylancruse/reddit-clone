from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'index.html', {
        'posts': posts
    })

def detail(request):
    return render(request, 'detail.html')

@login_required
def create(request):
    if request.method == "POST":
        pass

    form = PostForm()
    return render(request, 'create.html', {
        'form': form
    })