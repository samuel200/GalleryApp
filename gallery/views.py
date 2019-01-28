from django.shortcuts import render
from showcase.models import Post

def home(request):
    posts = Post.objects.all().order_by("-date")
    post_size = len(posts)

    return render(request, "index.html", {
                                            "posts": posts,
                                            "post_size": post_size,
                                            })
