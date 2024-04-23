from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User, related_name='user_blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category_blogs', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tag_blogs')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='blog_images/')

    def __str__(self):
        return self.blog.title
