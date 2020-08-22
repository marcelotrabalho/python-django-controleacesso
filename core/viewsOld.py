from django.shortcuts import render, HttpResponse, redirect
from core.models import Sistema
#https://tutorial.djangogirls.org/pt/django_start_project/

# Create your views here.
def index(request,nome, idade):
    return HttpResponse("<h1>inicio novo {} de {} anos</h1>".format(nome,idade))

def home(request):
    sistemas = Sistema.objects.all()
    dados = {"Sistemas": sistemas}
    return render(request,"home.html",dados)