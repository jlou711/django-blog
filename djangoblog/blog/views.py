from django.shortcuts import render
import datetime

# Create your views here.

posts = [
    {
        'author': 'Jamie Lou',
        'title': 'First Post',
        'body': 'This is my first post',
        'date_posted' : datetime.date.today()
    },
    {
        'author': 'Jamie Lou',
        'title': 'Second Post',
        'body': 'This is my second post',
        'date_posted' : datetime.date.today() + datetime.timedelta(days=1)
    }
]

def home(request):
    context = {
        'title': 'Blog-Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Blog-About'
    }
    return render(request, 'blog/about.html', context)