from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import  datetime
# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birday = models.DateField(verbose_name="生日",null=True,blank=True) #这个字段可以为空 blank null一般成对出现
    gender = models.CharField(max_length=10,choices=(("male","男"),("female","女"),),default="female") #choices默认显示一个选择框
    address = models.CharField(max_length=100,default="") #地址
    mobile = models.CharField(max_length=11,null=True,blank=True) #手机号
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100) #存头像字段

    class Meta:
        verbose_name = "用户信息"  #在web展示的时候 展示为"用户信息"
        verbose_name_plural = verbose_name #这个是复数形式，默认为verbose_name后面加s


    def __str__(self):
        return self.username

#邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name="邮箱")
    send_type = models.CharField(choices=(("register","注册"),("forget","找回密码"),),max_length=10,verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name="发送时间")
    #datetime.now根据class实例化的时间生成，datetime.now()带括号的就是根据model编译的时间生成


    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name



#轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图",max_length=100) #保存数据库存储的是路径地址
    url = models.URLField(max_length=200,verbose_name="访问地址")#点击之后的url跳转
    index = models.IntegerField(default=100,verbose_name="顺序") #控制轮播图顺序
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间") #生成时间

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name



