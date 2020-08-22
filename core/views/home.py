from django.shortcuts import render, HttpResponse, redirect
from core.models import Sistema

def inicio(request):
    sistemas = Sistema.objects.all()
    dados = {"Sistemas": sistemas}
    return render(request,"home.html",dados)