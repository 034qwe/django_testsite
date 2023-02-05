# Generated by Django 4.1.5 on 2023-02-05 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('anons', models.CharField(max_length=250, verbose_name='beginning')),
                ('main_text', models.TextField(verbose_name='article')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d', verbose_name='photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.category_articles')),
            ],
        ),
    ]
