# Generated by Django 2.2 on 2021-04-27 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iToys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('age', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_adds', to='iToys.User')),
                ('members', models.ManyToManyField(related_name='add', to='iToys.User')),
            ],
        ),
    ]
