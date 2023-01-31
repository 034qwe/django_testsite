from django.db import models
from django.urls import reverse
# Create your models here.


class Articles(models.Model):
    title=models.CharField('title',max_length=40)
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")
    anons =models.CharField('beginning',max_length=250)
    main_text=models.TextField('article')
    photo = models.ImageField('photo', upload_to="photos/%Y/%m/%d")
    date = models.DateField('date of publication',auto_created=True)
    categ = models.ForeignKey('Category_Articles',on_delete=models.PROTECT,null=True) #+= _id
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title


class Category_Articles(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs={'url_id':self.slug})

    def __str__(self):
        return self.name



