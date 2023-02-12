from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
# Create your views here.


class DataPage(ListView):
    model = Articles
    template_name = 'data/data_full.html'
    context_object_name = 'articles'


# def data(request):
#     all_articles = Articles.objects.all()
#     return render(request,'data/data_full.html',{'articles':all_articles,})

def login(request):
    return HttpResponse('login page')


class AddPage(CreateView):
    form_class =  ArticlesForm
    template_name = 'data/add.html' 
    success_url = reverse_lazy('data')

# def add(request):
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST,request.FILES)
#         if form.is_valid():
#                 form.save()
#                 return redirect('/')
#         else:
#             HttpResponse('error')
        
#     else:
#         form = ArticlesForm()
#     context = {
#         'form':form
#     }
#     return render(request,'data/add.html',context)



def show_category(request,cat_name):
    data_articles=Articles.objects.filter(slug=cat_name)
    data = {
        "data_art":data_articles, 
        'cat_selected':cat_name
        }
    return render(request,'data/data.html',data)

def show_post(request,post_slug):
    post = get_object_or_404(Articles,slug=post_slug) 
    contxt = {
        'post':post,
    }

    return render(request,'data/detail_view.html',context=contxt )


class ShowPost(DetailView):
    model = Articles #my database
    template_name = 'data/detail_view.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class DataUpdatelView(UpdateView):
    model = Articles
    template_name = 'data/add.html'
    
    form_class = ArticlesForm #fields in forms.py.ArticlesForm  


class DataDeletelView(DeleteView):
    model = Articles
    template_name = 'data/delete.html'
    success_url = '/'

