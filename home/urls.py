from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("", views.index, name='index'),
    path("login", views.loginn, name='login'),
    path("signup", views.signup, name='signup'),
]