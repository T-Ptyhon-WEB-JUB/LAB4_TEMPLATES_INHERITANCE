import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import secrets
# Create your views here.
def base (request):
    return (
        render(request,'home/base.html')  #to return a templete
    )

def today (request):
    return (
        render(request,'home/todayDate.html',{'today':date.today})  #to return a templete
    )

def password(request):
    passwordlen=10
    return(
        render(request,'home/pass.html',{'pass':secrets.token_urlsafe(passwordlen)})
    ) 

def favBooks(request):
    booksList=['book1','book2','book3']
    return(
        render(request,'home/fav.html',{'books':booksList})
    )

