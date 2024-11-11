from django.shortcuts import render, redirect
from app_login.models import Login

def index(request):
    return render(request, 'login/index.html')
