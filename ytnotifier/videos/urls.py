from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.KeyWordViewSet)

urlpatterns = [
    url('(?P<kw>.+)/videos', views.VideosView.as_view()),
] + router.urls
