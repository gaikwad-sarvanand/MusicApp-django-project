from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import render, redirect
from .models import SongForm, SongModel
from .serializer import SongSerializer


# Create your views here.


def add_song(request):
    if request.method == 'POST':
        f = SongForm(request.POST, request.FILES)
        f.save()
        return redirect("/")
    else:
        context = {'form': SongForm}
        return render(request, "add_song.html", context)


def song_list(request):
    e = SongModel.objects.all()
    context = {'el': e}
    return render(request, "songlist.html", context)


def delete_song(request, id):
    song = SongModel.objects.get(id=id)
    song.delete()
    return redirect("/song_list")


def update_song(request, id):
    song = SongModel.objects.get(id=id)
    if request.method == 'POST':
        f = SongForm(request.POST, request.FILES, instance=song)
        f.save()
        return redirect("/song_list")
    else:
        context = {'form': SongForm(instance=song)}
        return render(request, "add_song.html", context)


class CreateListSong(generics.ListCreateAPIView):
    queryset = SongModel.objects.all()
    serializer_class = SongSerializer


class UpdateDeleteGetSong(generics.RetrieveUpdateDestroyAPIView):
    queryset = SongModel.objects.all()
    serializer_class = SongSerializer


def song_library(request):
    if request.method == 'POST':
        search = request.POST['search'].capitalize()
        el = SongModel.objects.filter(song_name__contains=search)
        return render(request, "songs.html", {'el': el})
    el = SongModel.objects.all()
    return render(request, "songs.html", {'el': el})
