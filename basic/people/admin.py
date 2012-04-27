from django.contrib import admin
from basic.people.models import *


class PersonTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(PersonType, PersonTypeAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_filter = ('person_types',)
    search_fields = ('first_name', 'middle_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name', 'middle_name', 'last_name')}
admin.site.register(Person, PersonAdmin)

