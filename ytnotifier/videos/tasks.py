from __future__ import absolute_import, unicode_literals
import requests
from celery import task
from django.utils.dateparse import parse_datetime

from videos.models import KeyWord, Video


@task(name='save_videos')
def save_videos(keyword):
    params = {'part': 'snippet', 
              'q': keyword, 
              'type': 'video', 
              'key': 'AIzaSyAVnNYiiV55aUzoZAvKg7HwyC26pp19API'}
    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    for i in r.json().get('items'):
        vid_id = i.get('id').get('videoId')
        vid_ttl = i.get('snippet').get('title')
        vid_timestamp = parse_datetime(i.get('snippet').get('publishedAt'))
        vid, created = Video.objects.get_or_create(
            title=vid_ttl, 
            url=get_url(vid_id))
        vid.keywords.add()


@task(name='keyword_queries')
def keyword_queries():
    """Run save_videos async task for every keyword in the db"""
    keywords = KeyWord.objects.all()
    for kw in keywords:
        print(kw.word)
        save_videos.delay(kw.word)

def get_url(video_id):
    return 'https://www.youtube.com/watch?v=' + video_id
