# Generated by Django 5.0.4 on 2024-04-22 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_image_alter_blogimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]