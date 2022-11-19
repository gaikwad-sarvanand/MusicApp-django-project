from rest_framework import generics
from django.shortcuts import render, redirect
from .models import AlbumForm, AlbumModel
# from django.http import JsonResponse
from .serializers import AlbumSerializer
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# Create your views here.


def add_album(request):
    if request.method == 'POST':
        f = AlbumForm(request.POST, request.FILES)
        f.save()
        return redirect("/")
    else:
        f = AlbumForm
        context = {'form': f}
        return render(request, "add_album.html", context)


def album_list(request):
    e = AlbumModel.objects.all()
    context = {'el': e}
    return render(request, "albumlist.html", context)


def delete_album(request, id):
    song = AlbumModel.objects.get(id=id)
    song.delete()
    return redirect("/albumlist")


def update_album(request, id):
    song = AlbumModel.objects.get(id=id)
    if request.method == 'POST':
        f = AlbumForm(request.POST, request.FILES, instance=song)
        f.save()
        return redirect("/albumlist")
    else:
        context = {'form': AlbumForm(instance=song)}
        return render(request, "add_album.html", context)
# Create your views here.


# @api_view(['GET', 'POST'])
# def album_list_api(request):

#     if request.method == 'GET':
#         album = AlbumModel.objects.all()
#         serializer = AlbumSerializer(album, many=True)
#         return JsonResponse({'albums': serializer.data})

#     if request.method == 'POST':
#         serializer = AlbumSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CreateListAlbum(generics.CreateAPIView):
#     serializer_class = AlbumSerializer


class CreateListAlbum(generics.ListCreateAPIView):
    queryset = AlbumModel.objects.all()
    serializer_class = AlbumSerializer


class UpdateDeleteGetAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumModel.objects.all()
    serializer_class = AlbumSerializer


# class AlbumViewSet(viewsets.ModelViewSet):
#     queryset = AlbumModel.objects.all()
#     serializer_class = AlbumSerializer


def album_library(request):
    if request.method == 'POST':
        search = request.POST['search'].capitalize()
        album = AlbumModel.objects.filter(album_name__contains=search)
        return render(request, "albums.html", {'album': album})
    album = AlbumModel.objects.all()
    return render(request, "albums.html", {"album": album})
