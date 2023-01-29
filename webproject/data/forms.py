from .models import Articles
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