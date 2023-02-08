from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from .models import *
from .forms import *
from django.views.generic import DetailView,UpdateView,DeleteView,ListView
# Create your views here.

def data(request):
    all_articles = Articles.objects.all()
    cats = Category_Articles.objects.all()
    return render(request,'data/data_full.html',{'articles':all_articles,'cats':cats,})

def login(request):
    return HttpResponse('login page')

def add(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                return redirect('/')
        else:
            HttpResponse('error')
        
    else:
        form = ArticlesForm()
    context = {
        'form':form
    }
    return render(request,'data/add.html',context)

def show_category(request,url_id):
    data_articles=Articles.objects.filter(slug=url_id)
    cats = Category_Articles.objects.all()
    data = {
        "data_art":data_articles,
        'cats':cats,
        'cat_selected':url_id
        }
    return render(request,'data/data.html',data)

def show_post(request,post_slug):
    post = get_object_or_404(Articles,slug=post_slug) 
    contxt = {
        'post':post,
        "cat_selected": post.categ_id
    }

    return render(request,'data/detail_view.html',context=contxt )


# class DataDetailView(DetailView):
#     model = Articles #my database
#     template_name = 'data/detail_view.html'
#     context_object_name = 'post' #data_view.html h1


class DataUpdatelView(UpdateView):
    model = Articles
    template_name = 'data/add.html'
    
    form_class = ArticlesForm #fields in forms.py.ArticlesForm  


class DataDeletelView(DeleteView):
    model = Articles
    template_name = 'data/delete.html'
    success_url = '/'

