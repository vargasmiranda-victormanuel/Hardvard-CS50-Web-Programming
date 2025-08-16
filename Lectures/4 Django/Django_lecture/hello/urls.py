from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("vic",views.vic, name="vic"),
    path("<str:name>", views.greet, name="greet"),
]