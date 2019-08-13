from django.shortcuts import render, get_object_or_404, redirect
from .models import Cinema, Category
from . import views
def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'Cinemas': Cinema.objects.all()
    }
    return render(request, 'cinema/index.html', context)

def Cinema_detail(request, Cinema_id):
    post = get_object_or_404(Cinema, pk=Cinema_id)
    context = {
        'title': post,
        'post': post
    }
    return render(request, 'cinema/detail.html', context)


