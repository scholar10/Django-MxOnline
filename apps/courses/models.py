from django.db import models
from datetime import  datetime
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情") #textfield可以不输入长度，多长都可以
    degree = models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2,verbose_name="课程难度") #课程难度字段
    learn_times = models.IntegerField(default=0,verbose_name="学习时长(分钟数)") #时长字段
    students = models.IntegerField(default=0,verbose_name="学习人数") #学习人数字段\
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数") #收藏人数字段
    image = models.ImageField(upload_to="course/%Y/%m",verbose_name="封面图",max_length=100)#upload_to是指定保存的路径
    click_num = models.IntegerField(default=0,verbose_name="点击数") #点击数字段
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间") #记录添加时间

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    # FileField()是文件类型字段，在后台管理系统中直接就生成了上传的按钮，upload_to是上传的地址
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name="资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


