from django.db import models

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
    photo = models.ImageField('photo', upload_to="photos/%Y/%m/%d")
    date = models.DateField('date of publication',auto_now=True)


    def __str__(self):
        return self.name
    