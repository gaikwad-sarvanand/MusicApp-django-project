from rest_framework import serializers
from .models import AlbumModel


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = "__all__"
