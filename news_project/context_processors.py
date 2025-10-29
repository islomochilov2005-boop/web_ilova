from .models import Category

def all_Categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context  