from django.shortcuts import render,redirect, HttpResponse
from .models import Articles,Scientists,Category
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView
# Create your views here.

def data(request):
    cats = Category.objects.all()
    return render(request,'data/data.html',{'cats':cats})

def data_scientists(request):
    data_s  = Scientists.objects.all()
    data_sience = {
        'scientists':data_s,
        }
    return render(request,'data/data_scientists.html',data_sience)


def login(request):
    return HttpResponse('login page')

def add(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'incorrect'
    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request,'data/add.html',data)

def show_category(request,cat_id):
    data_articles=Scientists.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {
        "data_art":data_articles,
        'cats':cats,
        'cat_selected':cat_id
        }
    return render(request,'data/data.html',data)


class DataDetailView(DetailView):
    model = Articles #my database
    template_name = 'data/detail_view.html'
    context_object_name = 'post' #data_view.html h1


class DataUpdatelView(UpdateView):
    model = Articles
    template_name = 'data/add.html'

    form_class = ArticlesForm #fields in forms.py.ArticlesForm  


class DataDeletelView(DeleteView):
    model = Articles
    template_name = 'data/delete.html'
    success_url = '/'
