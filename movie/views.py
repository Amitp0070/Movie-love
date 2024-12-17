from django.shortcuts import render
from .models import Movies, Categories


def home(request):
    movie = Movies.objects.all()
    category = Categories.objects.all().order_by('title')
    return render(request, 'components/home.html', {"movie" : movie, "category": category})