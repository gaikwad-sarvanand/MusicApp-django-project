from django.db import models
from django import forms
from django.db import models
from artist_app.models import ArtistModel, ArtistForms


# Create your models here.
class SongModel(models.Model):
    song_profile_img = models.ImageField(upload_to="song_info", default="")
    song_name = models.CharField(max_length=50)
    song_length = models.CharField(max_length=20)
    song_genre = models.CharField(max_length=100)
    song_file = models.FileField(upload_to="song_audio")
    song_released = models.DateField(max_length=30, default="-")
    song_writer = models.CharField(max_length=200, default="-")
    song_label = models.CharField(max_length=100, default="-")
    # artist_name = models.ManyToManyField(ArtistModel, through='ArtistModel')
    artists = models.ManyToManyField(ArtistModel)

    def __str__(self):
        return self.song_name

    class Meta:
        db_table = "song_table"


class SongForm(forms.ModelForm):
    class Meta:
        model = SongModel
        fields = "__all__"
