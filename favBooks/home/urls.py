from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.base,name='home'),
    path('today/',views.today,name='home'),
    path('random/password/',views.password,name='home'),
    path('favs/books/',views.favBooks,name='home'),
]