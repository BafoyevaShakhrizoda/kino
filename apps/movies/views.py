from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Avg
from django.urls import reverse

from apps.movies.models import Movie, Review


def movies_view(request):
    search = request.GET.get('search')
    if search:
        movies = Movie.objects.filter(title__icontains=search)
    else:
        movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies': movies})


def single_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    rating = reviews.aggregate(Avg('rating'))
    return render(request, 'movie.html', context={'movie': movie, 'rating':rating['rating__avg'], 'ratings': range(1,11),'reviews': reviews})

def add_review_view(request,pk):
    comment = request.POST.get('comment')
    rating = request.POST.get('rating')
    name = request.POST.get('name')
    email = request.POST.get('email')
    movie = Movie.objects.get(id=pk)
    
    Review.objects.create (
                        movie=movie,
                        comment=comment,
                        rating=rating,
                        name=name,
                        email=email,
                       
                        )

    return redirect(reverse('single_movie', kwargs={'pk': pk}))