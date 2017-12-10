from django.contrib import admin

from mgallery.models import Movie


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(Movie, MovieAdmin)
