from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello World!</h1>')
    posts = Post.objects.all()[:10]
    context = {
        'title':'Latest Posts 1',
        'posts':posts
    }
    return render(request,'posts/index.html',context)
def details(request,id):
    post = Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'posts/detail.html',context)