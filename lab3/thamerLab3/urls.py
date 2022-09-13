from importlib.resources import path
from django.urls import path
from . import views

app_name = "thamerLab3"

urlpatterns = [
    path("", views.home, name = "home"),
    path("today/", views.today, name= "today"),
    path("random/password/", views.password, name= "password"),
    path("favs/books/", views.books, name = 'books'),
    path("about/", views.about, name = 'about')
]