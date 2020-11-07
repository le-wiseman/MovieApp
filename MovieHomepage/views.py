from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response1 = requests.get('https://api.themoviedb.org/3/trending/all/day?api_key=2bca7835c548e3242e8ccc0aa44a0513').json()
    response2 = requests.get('https://api.themoviedb.org/3/trending/all/week?api_key=2bca7835c548e3242e8ccc0aa44a0513').json()
    response3 = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=2bca7835c548e3242e8ccc0aa44a0513&language=en-US').json()
    return render(request, 'index.html', {'response1':response1,'response3':response3,'response2':response2})


def blogdetails(request):
    return render(request, 'blog-details.html')


def blog(request):
    return render(request, 'blog.html')


def celebrities(request):
    response = requests.get('https://api.themoviedb.org/3/person/popular?api_key=2bca7835c548e3242e8ccc0aa44a0513&language=en-US').json()
    return render(request, 'celebrities.html',{'response':response})


def moviedetails(request):
    return render(request, 'movie-details.html')


def movies(request):
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=2bca7835c548e3242e8ccc0aa44a0513&language=en-US&sort_by=popularity.desc&include_adult=true&include_video=true&year=2020').json()
    return render(request, 'movies.html', {'response':response})

def topmovies(request):
    response = requests.get('https://api.themoviedb.org/3/trending/movie/day?api_key=2bca7835c548e3242e8ccc0aa44a0513&page=2').json()
    return render(request, 'top-movies.html', {'response':response})
