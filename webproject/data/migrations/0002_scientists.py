# Generated by Django 4.1.5 on 2023-01-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scientists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('bio', models.TextField(verbose_name='bio')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='photo')),
                ('date', models.DateField(auto_now=True, verbose_name='date of publication')),
            ],
        ),
    ]