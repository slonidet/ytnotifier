from django.core import serializers
from rest_framework import mixins
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import KeyWord, Video
from .serializers import KeyWordSerializer, VideoSerializer


class KeyWordViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = KeyWordSerializer
    queryset = KeyWord.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        try:
            kw = KeyWord.objects.get(word=request.POST['word'])
            kw.users.add(user)
            kw.save()
            return Response('Keyword added to your list', status=status.HTTP_200_OK)
        except KeyWord.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.data['users'] = user
            return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(users__in=[self.request.user])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VideosView(ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if not KeyWord.objects.filter(users__in=[request.user], id=kwargs['kw']).exists():
            return Response('This keyword not in your list', status=status.HTTP_403_FORBIDDEN)
        qeuryset = self.queryset.filter(keywords__in=[kwargs['kw']])
        return super().get(self, request, *args, **kwargs)
