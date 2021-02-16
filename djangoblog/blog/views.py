from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    context = {
        'title': 'Blog-Home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Blog-About'
    }
    return render(request, 'blog/about.html', context)