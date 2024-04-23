from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Login MIXIN
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# from account.mixins import LogoutRequiredMixin

# forms
from django.contrib.auth.forms import AuthenticationForm

# models
from django.contrib.auth.models import User
from home.models import Blog, Category, Tag

# message
from django.contrib import messages

import uuid
from django.db.models import Q

# Create your views here


def home(request):
    blogs = Blog.objects.all().order_by('-id')
    tags = Tag.objects.all()
    latest_blog = Blog.objects.all()[:3]
    
    search_item = request.GET.get('search')
    
    if search_item:
        blogs = Blog.objects.filter(title__startswith=search_item)

    context = {
        'blogs': blogs,
        'tags': tags,
        'latest_blog': latest_blog,
        'search_item':search_item
    }
    return render(request, 'home/home.html', context)



def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }
    return render(request, 'home/blog_details.html', context)




def category_blog(request, slug):
    category = get_object_or_404(Category, slug=slug)
    cate_blogs = category.category_blogs.all()
    tags = Tag.objects.all()

    print(cate_blogs)
    print(tags)

    context = {
        'category': category,
        'cate_blogs': cate_blogs,
        'tags': tags
    }
    return render(request, 'home/category_blogs.html', context)


def tag_blog(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    tag_blogs = tag.tag_blogs.all()

    tags = Tag.objects.exclude(title=tag)

    print(tag_blogs)

    context = {
        'tag_name': tag,
        'tag_blogs': tag_blogs,
        'tags': tags

    }
    return render(request, 'home/tag_blogs.html', context)
