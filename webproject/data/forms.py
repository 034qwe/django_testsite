from .models import *
from django import forms
from django.forms import ModelForm,TextInput,DateInput,Textarea,ImageField


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','photo','main_text','date']

        widgets = { 
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'title',
            }),
            'anons' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'anons',
            }),
            'full_text' : Textarea(attrs={ 
                'class' : 'form-control',
                'placeholder': 'article',
            }),
            'date' : DateInput(attrs={
                'class' : 'form-control',
                'placeholder': 'date',
            }),

        }
    


class AddPost(forms.Form):
    title = forms.CharField(max_length=40)
    slug = forms.SlugField(max_length=255,)
    anons =forms.CharField(max_length=250)
    main_text=forms.Textarea()
    categ = forms.ModelChoiceField(queryset=Category_Articles.objects.all())
    is_published = forms.BooleanField() 