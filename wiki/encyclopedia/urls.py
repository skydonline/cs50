from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pagename>", views.page, name="pagename"),
    path("search/", views.search, name="search"),
]
