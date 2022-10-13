from rest_framework import serializers
from .models import Poster

class PosterCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Poster
        fields = ('id', 'name', 'image', 'user_fk')

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'