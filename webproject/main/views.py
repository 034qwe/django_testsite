from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'main/list.html')

def me(request):
    return render(request,'main/list2.html')