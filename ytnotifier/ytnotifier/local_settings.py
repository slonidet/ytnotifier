from ytnotifier.settings import *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ytnotifier',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',  
        'PORT': '3306',
    }
}


YOUTUBE_API_KEY = 'AIzaSyAVnNYiiV55aUzoZAvKg7HwyC26pp19API'
