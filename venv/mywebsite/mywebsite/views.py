# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm

def welcome(request):
    return render(request, 'welcome.html', {'current_date_time':datetime.now, 'name':'Nassim'})

def login(request):
    #teste si le formulaire a été envoyé
    if len(request.POST) >0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/welcome')
        else:
            return render(request,'login.html',{'form':form})
    else:
        form=LoginForm()
        return render(request, 'login.html', {'form':form})