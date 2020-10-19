from django.shortcuts import render, redirect
from django.conf.urls import url
from .models import Items
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    ite=Items.objects.all()
    return render(request,"index.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def pr(request):
    ite=Items.objects.all()
    context={'ite':ite}
    return render(request,"pr.html",context)