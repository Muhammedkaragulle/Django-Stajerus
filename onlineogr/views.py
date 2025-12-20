from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'anasayfa.html')


def ulas(request):
    return render(request, 'bizeulasin.html')    

def hakkimiz(request):
    return render(request, 'hakkimizda.html')    