from django.contrib import admin
from .models import Lesson, Course, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Lesson)
class PostAdmin(SummernoteModelAdmin):
    """
    Fileds for search, field filters, field to populate
    and text editor
    """

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Course)
admin.site.register(Comment)