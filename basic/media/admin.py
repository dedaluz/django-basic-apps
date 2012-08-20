from django.contrib import admin
from basic.media.models import *


class AudioSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(AudioSet, AudioSetAdmin)


class AudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Audio, AudioAdmin)


class PictureSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(PictureSet, PictureSetAdmin)


class PictureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Picture, PictureAdmin)


class VideoSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(VideoSet, VideoSetAdmin)


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Video, VideoAdmin)