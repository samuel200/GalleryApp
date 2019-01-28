from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/signin/")
def index(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "showcase/index.html", {"posts": posts})

def post_details(request, title):
    post = Post.objects.get(title=title)
    return render(request, "showcase/post_details.html", {"post": post})
