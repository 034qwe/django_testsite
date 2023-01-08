from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField('title',max_length=40)
    anons =models.CharField('beginning',max_length=250)
    main_text=models.TextField('article')
    date = models.DateField('date of publication')

    def __str__(self):
        return self.title
