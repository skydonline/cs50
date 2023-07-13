from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pagename>", views.page, name="pagename"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("add_page/", views.add_page, name="add_page"),
    path("edit_page/<str:pagename>", views.edit_page, name="edit_page"),
    path("random_page/", views.random_page, name="random_page"),
]
