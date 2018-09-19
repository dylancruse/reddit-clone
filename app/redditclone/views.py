from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

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
    return render(request, 'create.html')