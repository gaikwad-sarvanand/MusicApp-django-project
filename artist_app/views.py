from django.shortcuts import render
from tkinter import E
from django.shortcuts import render, redirect
from .models import ArtistForms, ArtistModel
# from.serializer import ArtistSerializer
from rest_framework import generics
from .serializer import ArtistSerializer

# Create your views here.


def add_artist(request):
    if request.method == 'POST':
        e = ArtistForms(request.POST, request.FILES)
        e.save()
        return redirect("/")
    else:
        f = ArtistForms
        context = {'form': f}
        return render(request, "artist_form.html", context)


def artist_list(request):
    el = ArtistModel.objects.all()
    context = {'el': el}
    return render(request, "artist_list.html", context)


def artist_library(request):
    if request.method == 'POST':
        search = request.POST['search'].capitalize()
        el = ArtistModel.objects.filter(artist_name__contains=search)
        return render(request, "artists.html", {'el': el})
    el = ArtistModel.objects.all()
    return render(request, "artists.html", {'el': el})


def delete_artist(request):
    eid = request.GET.get("id")
    emp = ArtistModel.objects.get(id=eid)
    emp.delete()
    return redirect("/artist_list")


def update_artist(request, id):
    emp = ArtistModel.objects.get(id=id)
    if request.method == 'POST':
        f = ArtistForms(request.POST, request.FILES, instance=emp)
        f.save()
        return redirect("/artist_list")
    else:
        context = {'form': ArtistForms(instance=emp)}
        return render(request, "artist_form.html", context)


class CreateListArtist(generics.ListCreateAPIView):
    queryset = ArtistModel.objects.all()
    serializer_class = ArtistSerializer


class UpdateDeleteGetArtist(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistModel.objects.all()
    serializer_class = ArtistSerializer
