from django.db import models
from datetime import  datetime
from  users.models import UserProfile
from courses.models import Course

# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")
    mobile = models.CharField(max_length=11,verbose_name="手机")
    course_name = models.CharField(max_length=50,verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    """课程评论表"""
    user = models.ForeignKey(UserProfile,verbose_name="用户",on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    comments = models.CharField(max_length=200,verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论" #定义表名称
        verbose_name_plural = verbose_name



class UserFavorite(models.Model):
    """用户收藏表"""
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")),default=1,verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"  # 定义表名称
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name="接收用户")
    message = models.CharField(max_length=500,verbose_name="消息内容")
    has_read = models.BooleanField(default=False,verbose_name="是否已读")#布尔类型变量前面加个has
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"  # 定义表名称
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """记录用户的学习课程"""
    user = models.ForeignKey(UserProfile,verbose_name="用户",on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户课程"  # 定义表名称
        verbose_name_plural = verbose_name
