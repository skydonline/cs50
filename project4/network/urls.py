
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpost", views.new_post, name='new_post'),
    path("profile/<int:user_profile>", views.profile, name='profile'),
    path("following_posts", views.following_posts, name='following_posts'),

    #APIs
    path('api/all_posts/', views.all_posts_api, name='all_posts_api'),
]
