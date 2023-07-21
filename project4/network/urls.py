
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
    path("settings", views.settings, name='settings'),
    path("change_password", views.change_password, name="change_password"),

    #APIs
    path('api/all_posts/', views.all_posts_api, name='all_posts_api'),
    path('api/post/<int:postID>', views.post_api, name="post_update"),
    path('api/followers/<int:profile>', views.followers, name='followers'),
    path('api/following/<int:profile>', views.following, name='following'),
    path('api/password/<int:userID>', views.password, name="password"),
    path('api/settings/<int:userID>', views.settings_api, name="settings")
]
