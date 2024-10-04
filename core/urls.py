from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.settings, name="settings"),
    path('upload/', views.upload, name="upload"),
    path('like-post/', views.like_post, name="like-post"),
    path('like-post/', views.follow, name="follow"),
    path('follow', views.profile, name="profile"),
    path('settings/', views.settings, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),



]
