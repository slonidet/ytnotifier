from django.contrib import admin

from .models import KeyWord, Video


class KeyWordAdmin(admin.ModelAdmin):
	list_display = ('id', 'word',)


class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'url')


admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(Video, VideoAdmin)
