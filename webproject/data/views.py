from django.shortcuts import render
from .models import Articles

# Create your views here.

def data(request):
    data_articles=Articles.objects.all()
    return render(request,'data/data.html',{"data_art":data_articles})


def add(request):
    return render(request,'data/add.html')