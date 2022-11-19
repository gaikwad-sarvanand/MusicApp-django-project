from django.db import models

# Create your models here.
from django import forms
from distutils.command.upload import upload
from django.db import models
from song_app.models import SongForm, SongModel, ArtistForms, ArtistModel

# Create your models here.


class AlbumModel(models.Model):
    album_profile = models.ImageField(upload_to="album_profile", default="")
    album_name = models.CharField(max_length=30)
    album_genre = models.CharField(max_length=20)
    album_released = models.DateField(max_length=30, default="-")
    album_label = models.CharField(max_length=50, default="-")
    album_producer = models.CharField(max_length=150, default="-")
    album_songs = models.ManyToManyField(SongModel)
    album_artist = models.ManyToManyField(ArtistModel)

    def __str__(self):
        return self.album_name

    class Meta:
        db_table = "album_tb"


class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = "__all__"
