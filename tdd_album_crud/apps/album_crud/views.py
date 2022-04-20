from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "answer" : 42
    }
    return render(request, "index.html", context)
    

def create(request):
    if request.method == 'POST':
        Album.objects.create(title = request.POST['title'], artist = request.POST['artist'], year = request.POST['year'])

    return redirect('/')

def edit(request, id):
    if request.method == 'POST':
        album = Album.objects.get(id)
        print(album)
        album.title = request.POST['title']
        album.artist = request.POST['artist']
        album.year = request.POST['year']
        album.save()

    return redirect('/')