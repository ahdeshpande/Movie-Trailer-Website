from random import shuffle

from django.shortcuts import render

from mgallery.models import Movie
from mgallery.services import get_movie_data


# Create your views here.
def movies_website(request):
    movie_list = Movie.objects.all()

    if movie_list is None:
        all_movie_data = []
    else:
        all_movie_data = []
        for movie in movie_list:
            movie_data = get_movie_data(movie.title)
            all_movie_data.append(movie_data)
        shuffle(all_movie_data)

    return render(request,
                  'movie_website.html',
                  {'all_movies': all_movie_data})
