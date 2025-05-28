from django.contrib import admin
from apps.movies.models import Movie, Actor, Trailer, Genre

admin.site.register(Movie) 
admin.site.register(Actor) 
admin.site.register(Trailer) 
admin.site.register(Genre) 