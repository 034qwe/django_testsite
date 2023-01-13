from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
# Create your views here.

def data(request):
    data_articles=Articles.objects.all()
    return render(request,'data/data.html',{"data_art":data_articles})


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

class DataDetailView(DetailView):
    model = Articles #my database
    template_name = 'data/detail_view.html'
    context_object_name = 'post' #data_view.html h1
