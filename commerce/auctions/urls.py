from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("listing/<int:id>", views.listing, name='listing'),
    path('listing/<int:id>/<str:bid_success>', views.listing, name='bid_success'),
    path("watchlist", views.watchlist, name='watchlist'),
    path("bid/<int:id>", views.bid, name='bid'),
    path("close/<int:id>", views.close, name="close"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("categories", views.categories, name="categories"),
    path("categorypage/<int:id>", views.category_page, name="category_page"),
    path("settings/<str:settings_change>/<str:password_change>", views.settings, name="settings"),
    path("change_password", views.change_password, name='change_password')
]
