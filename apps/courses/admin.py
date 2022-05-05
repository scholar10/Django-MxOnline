from django.contrib import admin
from .models import *

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num','add_time']
    search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_num','add_time']
    #list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_num','add_time']



class LessonAdmin(admin.ModelAdmin):
    list_display = ['course','name','add_time']
    search_fields = ['course__name','name']
    list_filter = ['course__name','name','add_time']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson__name','name']
    list_filter = ['lesson__name','name','add_time']


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ['course','name','download','add_time']
    search_fields = ['course__name','name','download']
    list_filter = ['course__name','name','download','add_time']


admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(CourseResource,CourseResourceAdmin)
