from django.conf.urls import url
from . import views

app_name= "gallery"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^post_details/(?P<title>\w+)/$', views.post_details, name="post_details"),
]
