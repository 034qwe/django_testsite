from django.shortcuts import render


# Create your views here.
def index(request):
    data_c = {
        'title':'main page',
        
    }
    return render(request,'main/list.html',data_c)

def me(request):
    return render(request,'main/list2.html')