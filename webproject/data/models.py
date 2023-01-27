from django.db import models
from django.urls import reverse
# Create your models here.
class Articles(models.Model):
    title=models.CharField('title',max_length=40)
    anons =models.CharField('beginning',max_length=250)
    main_text=models.TextField('article')
    date = models.DateField('date of publication')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title


class Scientists(models.Model):
    name = models.CharField('name',max_length= 255)
    bio = models.TextField('bio')
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")
    photo = models.ImageField('photo', upload_to="photos/%Y/%m/%d")
    date = models.DateField('date of publication',auto_now=True) 
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True) #cat + _id

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk':self.pk})


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    