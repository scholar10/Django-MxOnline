from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile,EmailVerifyRecord
from  django.contrib.auth.hashers import make_password#调用函数对明文加密

from .forms import LoginForm,RegisterForm,ForgetForm,ModifyPwdForm
from utils.email_send import send_register_email

# Create your views here.
#用户名密码都可以登陆后台
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):   # 加密明文密码
                return user
        except Exception as e:
            return None


#邮件激活
class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:   #存在则激活
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else: #不存在则返回链接失效
            return render(request,"active_fail.html")

        return render(request,"login.html")





#邮箱注册
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm(request.POST)
        context = {'register_form':register_form}
        return render(request,"register.html",context)

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST['email']
            if UserProfile.objects.filter(email=user_name): #查询email是否被注册了
                context = {"msg": "用户已经存在","register_form":register_form}
                return render(request, 'register.html', context=context)

            pass_word = request.POST['password']
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False #用户设置为未激活，点击邮箱发送的链接以后才激活
            user_profile.password = make_password(pass_word)#输入的是明文，这里进行一个加密
            user_profile.save()#保存

            send_register_email(user_name,"register")
            return render(request, 'login.html')
        else:
            context = {"register_form":register_form}
            return render(request, 'register.html',context=context)


#登陆后台
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST) #会去做校验
        if login_form.is_valid(): #判断 是否通过form验证

            user_name = request.POST['username']
            pass_word = request.POST['password']
            # 验证用户名密码是否正确,认证成功会返回对象，认证失败返回none,并未真正完成登陆
            user = authenticate(request, username=user_name,password=pass_word)
            # 判断是否认证成功
            if user is not None:
                #判断是否激活了用户
                if user.is_active:
                    # 完成登陆
                    login(request, user)
                    # 登陆成功跳转首页
                    return render(request, "index.html")
                else:
                    context = {'msg':'用户未激活'}
                    return render(request, "login.html",context=context)
            else:
                context = {'msg': '账号或密码错误'}
                return render(request, 'login.html', context=context)
        else:
            context = {'login_form':login_form}
            return render(request, 'login.html', context=context)

#找回密码
class ForgetPwdView(View):
    def get(self,request):
        forget_form = ForgetForm()
        context = {'forget_form':forget_form}
        return render(request,'forgetpwd.html',context=context)

    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid(): #验证form表单是否合法，合法就发送邮件
            email = request.POST["email"]
            send_register_email(email,"forget")
            return render(request,'send_success.html')
        else:
            context = {'forget_form':forget_form}
            return render(request, 'forgetpwd.html', context=context)


#找回密码链接的get请求
class RestView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:   #存在跳转到重置密码界面
            for record in all_records:
                email = record.email
                context = {'email':email} #传email进去，让程序知道要重置哪个邮箱的密码
                return render(request,"password_reset.html",context=context)
        else: #不存在则返回链接失效
            return render(request,"active_fail.html")

        return render(request,"login.html")
#找回密码链接的get请求
class ModifyPwdView(View):
    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST['password']
            pwd2 = request.POST['password2']
            email = request.POST['email']
            if pwd1 != pwd2:
                context = {'email':email,'msg':'密码不一致'}
                return render(request,'password_reset.html',context=context)
            #如果两次密码一致则确认修改此邮箱的密码
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST['email']
            context = {'email': email, 'modify_form': modify_form}
            return render(request, 'password_reset.html', context=context)


# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST['username']
#         pass_word = request.POST['password']
#         user = authenticate(request,username=user_name,password=pass_word) #验证用户名密码是否正确,认证成功会返回对象，认证失败返回none,并未真正完成登陆
#         if user is not None: #判断是否认证成功
#             login(request,user) #完成登陆
#             return render(request,"index.html") #登陆成功跳转首页
#         else:
#             context = {'msg':'账号或密码错误'}
#             return render(request,'login.html',context=context)
#
#     elif request.method == "GET":
#         return render(request,'login.html')
