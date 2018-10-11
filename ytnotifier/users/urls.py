from django.conf.urls import url

from . import views


urlpatterns = [
    url('signup', views.UserCreateView.as_view(), name='signup'),
    url('login', views.AuthTokenView.as_view(), name='login'),
]
