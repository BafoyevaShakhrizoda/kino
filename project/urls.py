
from django.contrib import admin
from django.urls import path
from apps.movies.views import home,movies,movie
from apps.common.views import about,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movies/', movies, name='movies'),
    path ('movie/', movie, name='movie'),
    path('about/', about, name='about'),
    path('cntact', contact, name='contact'),
]
