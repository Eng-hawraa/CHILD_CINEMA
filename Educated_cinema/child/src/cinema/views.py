from django.shortcuts import render, get_object_or_404, redirect
from .models import Cinema, Category
from . import views
def home(request):
    if request.method=="POST":
        search_query = request.POST.get('search_box')
        cin = Cinema.objects.filter(name__icontains=search_query)
    else:
        cin = Cinema.objects.all()
    context = {
        'title': 'الصفحة الرئيسية',
        'Cinema': cin
    }
    return render(request, 'cinema/index.html', context)

def Cinema_detail(request, Cinema_id):
    post = get_object_or_404(Cinema, pk=Cinema_id)
    context = {
        'title': post,
    }
    return render(request, 'cinema/detail.html', context)
