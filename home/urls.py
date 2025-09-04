from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.loginn, name='login'),
    path("signup", views.signup, name='signup'),
]