from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import date
import secrets
# Create your views here.
def home(request):
    return render(request, 'base/base.html')
def today(request):
    today = date.today()
    return render(request, 'base/today.html', {'today': today})

def password(request):
    passLen = 12
    return render(request, 'base/pass.html', {'pass' : secrets.token_urlsafe(passLen)})

def books(request):
    book = ['thamer', 'ali', 'abduallh']
    return render(request, 'base/books.html', {'book': book})
def about(request):
    about = "csthamer.ba@gmail.com"
    return render(request, 'base/about.html', {'about': about})
