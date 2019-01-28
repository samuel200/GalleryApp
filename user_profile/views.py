from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PhotoPost

@login_required(login_url='account:signin')
def index(request):
    post_fields = PhotoPost()
    return render(request, "user_profiles/index.html", {"post_fields": post_fields})
