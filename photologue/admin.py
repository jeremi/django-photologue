""" Newforms Admin configuration for Photologue

"""
from django.contrib import admin
from models import *

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'photo_count', 'is_public')
    list_filter = ['date_added', 'is_public']
    date_hierarchy = 'date_added'
    prepopulated_fields = {'title_slug': ('title',)}
    filter_horizontal = ('photos',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'is_public', 'view_count', 'admin_thumbnail_view')
    list_filter = ['date_added', 'is_public']
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryUpload)
admin.site.register(Photo, PhotoAdmin)
