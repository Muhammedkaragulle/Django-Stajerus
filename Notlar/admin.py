from django.contrib import admin
from .models import Course, Note


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created')
    search_fields = ('name', 'user__username')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'course', 'created', 'updated')
    search_fields = ('title', 'content', 'user__username')
from django.contrib import admin

# Register your models here.
