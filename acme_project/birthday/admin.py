from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_displey = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_displey = ['tag']
