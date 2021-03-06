from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models import permalink
from django.contrib.auth.models import User
from taggit_autosuggest.managers import TaggableManager

from sorl.thumbnail import ImageField

import datetime
from dateutil import relativedelta

from basic.places.models import Place


class PersonType(models.Model):
    """Person type model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('person type')
        verbose_name_plural = _('person types')
        db_table = 'people_types'
        ordering = ('title',)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('person_type_detail', None, {'slug': self.slug})


class Person(models.Model):
    """Person model."""
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField(_('first name'), blank=True, max_length=100)
    middle_name = models.CharField(_('middle name'), blank=True, max_length=100)
    last_name = models.CharField(_('last name'), blank=True, max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    user = models.ForeignKey(User, blank=True, null=True, help_text='If the person is an existing user of your site.')
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    mugshot  = ImageField(_('picture'), upload_to='people_mugshots', blank=True)
    mugshot_credit = models.CharField(_('mugshot credit'), blank=True, max_length=200)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    origin_place = models.ForeignKey(Place, blank=True, null=True, related_name='origin_place')
    living_place = models.ForeignKey(Place, blank=True, null=True, related_name='living_place')
    person_types = models.ManyToManyField(PersonType, blank=True)
    website = models.URLField(_('website'), blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
        db_table = 'people'
        ordering = ('last_name', 'first_name',)

    def __unicode__(self):
        return u'%s' % self.full_name

    @property
    def full_name(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    @property
    def age(self):
        TODAY = datetime.date.today()
        if self.birth_date:
            return u"%s" % relativedelta.relativedelta(TODAY, self.birth_date).years
        else:
            return None

    @permalink
    def get_absolute_url(self):
        return ('person_detail', None, {'slug': self.slug})
