# Generated by Django 4.2 on 2023-07-26 00:24

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('desciption', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('tranding', models.BooleanField(default=False, help_text='0=default, 1=Tranding')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('prduct_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('small_desciption', models.CharField(max_length=250)),
                ('quantity', models.ImageField(upload_to='')),
                ('desciption', models.TextField(max_length=500)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('tranding', models.BooleanField(default=False, help_text='0=default, 1=Tranding')),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]