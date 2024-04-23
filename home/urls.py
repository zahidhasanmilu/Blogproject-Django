from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_details/<str:slug>/', views.blog_details, name='blog_details'),
    
    path('category/<str:slug>/', views.category_blog, name='category_blog'),
    path('tag/<str:slug>/', views.tag_blog, name='tag_blogs'),
]
