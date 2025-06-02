from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.specific_title, name='specific_title'),
    path("search/", views.search, name="search"),
    path("new_wiki_page/", views.new_wiki_page, name="new_wiki_page"),
    path("edit/", views.edit, name="edit"),
    path("save_page/", views.save_page, name="save_page"),
    path("random_page/", views.random_page, name="random_page"),
]