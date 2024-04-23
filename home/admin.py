from django.contrib import admin
from home.models import Category, Tag, Blog, BlogImage


class ImageInline(admin.StackedInline):
    '''Stacked Inline View for Image'''
    model = BlogImage
    min_num = 1
    
    


class BlogAdmin(admin.ModelAdmin):
    '''Admin View for Blog'''

    list_display = ['title', 'user', 'category',
                    'get_tags_display', 'created_date']

    inlines = [
        ImageInline,
    ]

    def get_tags_display(self, obj):
        return ', '.join(tag.title for tag in obj.tags.all())


# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
