from django.db import models
from django.db.models import permalink
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from taggit_autosuggest.managers import TaggableManager
from sorl.thumbnail import ImageField


class AudioSet(models.Model):
    """AudioSet model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    audios = models.ManyToManyField('Audio', related_name='audio_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_audio_sets'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('audio_set_detail', None, { 'slug': self.slug })


class Audio(models.Model):
    """Audio model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    still = models.FileField(upload_to='audio_stills', blank=True, help_text='An image that will be used as a thumbnail.')
    audio = models.FilePathField(path=settings.MEDIA_ROOT+'audios/', recursive=True)
    description = models.TextField(blank=True)
    tags = TaggableManager()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_audio'
        verbose_name_plural = 'audios'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
      return ('audio_detail', None, { 'slug': self.slug })


class PictureSet(models.Model):
    """PictureSet model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    cover_picture = models.ForeignKey('Picture', blank=True, null=True)
    pictures = models.ManyToManyField('Picture', related_name='picture_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
      db_table = 'media_picture_sets'

    def __unicode__(self):
      return '%s' % self.title

    @permalink
    def get_absolute_url(self):
      return ('picture_set_detail', None, { 'slug': self.slug })


class Picture(models.Model):
    """Picture model"""
    LICENSES = (
        ('http://creativecommons.org/licenses/by/2.0/',         'CC Attribution'),
        ('http://creativecommons.org/licenses/by-nd/2.0/',      'CC Attribution-NoDerivs'),
        ('http://creativecommons.org/licenses/by-nc-nd/2.0/',   'CC Attribution-NonCommercial-NoDerivs'),
        ('http://creativecommons.org/licenses/by-nc/2.0/',      'CC Attribution-NonCommercial'),
        ('http://creativecommons.org/licenses/by-nc-sa/2.0/',   'CC Attribution-NonCommercial-ShareAlike'),
        ('http://creativecommons.org/licenses/by-sa/2.0/',      'CC Attribution-ShareAlike'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = ImageField(verbose_name=_('image'), upload_to='images')
    taken_by = models.CharField(max_length=100, blank=True)
    license = models.URLField(blank=True, choices=LICENSES)
    description = models.TextField(blank=True)
    tags = TaggableManager()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    _exif = models.TextField(blank=True) 

    class Meta:
        db_table = 'media_pictures'

    def _set_exif(self, d):
        self._exif = simplejson.dumps(d)

    def _get_exif(self):
        if self._exif:
            return simplejson.loads(self._exif)
        else:
            return {}

    exif = property(_get_exif, _set_exif, "Picture EXIF data, as a dict.")

    def __unicode__(self):
        return '%s' % self.title

    @property
    def url(self):
        return '%s%s' % (settings.MEDIA_URL, self.picture)

    @permalink
    def get_absolute_url(self):
        return ('picture_detail', None, { 'slug': self.slug })


class VideoSet(models.Model):
    """VideoSet model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    videos = models.ManyToManyField('Video', related_name='video_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_video_sets'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('video_set_detail', None, { 'slug': self.slug })


class Video(models.Model):
    """Video model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    still = models.FileField(upload_to='video_stills', blank=True, help_text='An image that will be used as a thumbnail.')
    video = models.FilePathField(path=settings.MEDIA_ROOT+ '/uploads', recursive=True)
    description = models.TextField(blank=True)
    tags = TaggableManager()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_videos'

    def __unicode__(self):
        return '%s' % self.title
        
    def url(self):
        path = self._meta.get_field('video').path
        return self.video.replace(path, '', 1)
 

    @permalink
    def get_absolute_url(self):
        return ('video_detail', None, { 'slug': self.slug })
