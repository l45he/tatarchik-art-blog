from django.contrib import admin
from .models import Artworks, Images

# Register your models here.
class ArtworksAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_image')
	# list_display_links = ('title', 'content')
	# search_fields = ('title', 'content')

admin.site.register(Artworks, ArtworksAdmin)
admin.site.register(Images)