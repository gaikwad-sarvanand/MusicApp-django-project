from rest_framework import serializers
from .models import ArtistModel


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = "__all__"
