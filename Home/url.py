from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name="Home"),

    path('crypto', views.crypto, name="Home"),

    path('signup', views.signup, name="SignUp"),

    path('writer', views.writer, name="Writer_page"),

    path('coder', views.coder, name="Coder"),

    path('insta', views.insta, name="Insta"),
]
