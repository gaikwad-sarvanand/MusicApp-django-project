from django.db import models
# from album_app.models import AlbumModel
# from song_app.models import SongModel

# Create your models here.
from django import forms
from django.db import models

# Create your models here.


class ArtistModel(models.Model):
    artist_profile_img = models.ImageField(
        upload_to="artist_profile", default="")
    artist_name = models.CharField(max_length=50)
    artist_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.artist_name

    class Meta:
        db_table = "artist_tb"


class ArtistForms(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = "__all__"
