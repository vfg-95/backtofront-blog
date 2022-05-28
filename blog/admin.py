from django.contrib import admin
from . models import Post, Release
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'posted_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_on')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):

    list_display = ('title', 'cover_img')

