from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm,TextInput,DateInput,Textarea,ImageField


class ArticlesForm(ModelForm):

    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['categ'].empty_label = 'category not selected'
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 250:
            raise ValidationError("write shorter title please ")
        return title

    class Meta:    

        model = Articles
        fields = ['title','anons','main_text','photo','categ','slug']

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

        

        }
    



