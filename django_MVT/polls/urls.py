from django.urls import path
# from django.urls.resolvers import URLPATTERN
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]