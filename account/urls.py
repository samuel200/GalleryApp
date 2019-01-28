from django.conf.urls import url
from . import views

app_name= "account"

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signout/$', views.signout, name="signout"),
]
