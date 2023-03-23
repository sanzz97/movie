from django.http import HttpResponse
from django.shortcuts import render, redirect
from  . models import Movie
from . forms import MovieForm

# Create your views here.

def index(request): #to fetch all data from db admin
    movie = Movie.objects.all()
    context = {
        'movie_list' : movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    # return HttpResponse('this movie is no %s' % movie_id) #%s to print it as a string
    return render(request,'detail.html',{'movie':movie})

def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name') #we need to get all the details
        desc = request.POST.get('desc' )
        year = request.POST.get('year' )
        img = request.FILES['img'] #for img we need to use files
        movie = Movie(name=name,desc=desc,year=year,img=img) #after fetching all details we need to add it to database
        movie.save()


    return render(request,'add.html')

def update(request,id): #we are using id as for particular movie particular id will be there, so we can edit using id
    movie = Movie.objects.get(id=id) #to get all the id of the objects stored in movie table
    form = MovieForm(request.POST or None, request.FILES,instance=movie) #in instance we need to mention wat we need to edit
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})


def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete() #to delete the movie with the corresponding id
        return redirect('/') #after deleting return to homepage
    return render(request,'delete.html')