from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Under Construction')
    return render(request, 'index.html')