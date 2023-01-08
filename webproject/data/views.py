from django.shortcuts import render


# Create your views here.

def data(request):
    return render(request,'data/data.html')