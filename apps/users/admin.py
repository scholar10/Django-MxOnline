from django.contrib import admin
from .models import *

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code','email','send_type','send_time']#后台展示
    search_fields = ['code','email','send_type'] #搜索
    list_filter =  ['code','email','send_type','send_time'] #过滤器


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.site_header = '慕学后台管理系统'
admin.site.site_title = '慕学后台管理系统'
