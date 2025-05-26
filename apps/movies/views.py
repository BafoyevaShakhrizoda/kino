from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def movies(request):
    return render(request,'movies.html')

def movie(request):
    return render(request,'movie.html')


