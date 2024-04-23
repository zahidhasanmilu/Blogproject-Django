from home.models import Blog, Category, Tag


def get_all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context


