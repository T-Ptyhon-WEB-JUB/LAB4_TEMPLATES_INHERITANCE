from django.urls import path
from . import views

app_name = "lab3App"

urlpatterns = [
    path('', views.base, name="base"),
    path('today/', views.today, name="today"),
    path('password/', views.password, name="password"),
    path("books/", views.books, name="books")
    
]
