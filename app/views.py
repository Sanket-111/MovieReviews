import django
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Movie_info


# Create your views here.
def index(request):
    return render(request,"index.html")

def form_submissionat(request):
    movie_name=request.POST["movie_name"]
    movie_review=request.POST["movie_review"]
    movie_release=request.POST["movie_release"]
    movie_detail=request.POST["movie_detail"]
    hero_name=request.POST["hero_name"]
    heroin_name=request.POST["heroin_name"]

    movie_info=Movie_info(movie_name=movie_name ,movie_review=movie_review ,movie_release_date=movie_release, movie_detail=movie_detail, movie_hero=hero_name ,movie_heroin=heroin_name )
    movie_info.save()

    all_movies=Movie_info.objects.all()
    return render(request,"see.html",{'Movies':all_movies})        

def see(request):
    all_movies=Movie_info.objects.all()
    return render(request,"see.html",{'Movies':all_movies})    

def back(request):
    return render(request,"index.html")

def print(request):
    return render(request,"print.html")    

