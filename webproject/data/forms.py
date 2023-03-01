from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm,TextInput,DateInput,Textarea,ImageField
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


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
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'login'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'password'}))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'repeat password'}))
    class Meta:
        model = User
        fields = ('username','password1','password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'login'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'password'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'name'}))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'email'}))
    content = forms.CharField(label='text',widget=forms.Textarea(attrs={'class':'form-control','placeholder': ' questions or complaints'}))
    captcha = CaptchaField()