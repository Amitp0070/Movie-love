from django.shortcuts import render, get_object_or_404
from .models import Movies, Categories
from django.core.paginator import Paginator

def home(request):
    movie = Movies.objects.all().order_by("-create_at")
    category = Categories.objects.all().order_by('title')
    
    # Paginate movies with 10 movies per page
    paginator = Paginator(movie, 12)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    return render(request, 'components/home.html', {"movies": movies, "category": category})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    category = Categories.objects.all().order_by('title')
    return render(request, 'components/movie_detail.html', {'movie': movie, 'category': category})