from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='Home'),
    path('today/', views.today, name='today'),
    path('password/', views.passgen, name='password'),
    path('favs/book/', views.favbook, name='bookfavs'),
]