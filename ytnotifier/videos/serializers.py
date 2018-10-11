from rest_framework import serializers

from videos.models import KeyWord, Video


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('id', 'word',)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'url',)
