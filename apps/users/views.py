from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View

from .forms import LoginForm,RegisterForm

# Create your views here.



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
                # 完成登陆
                login(request, user)
                # 登陆成功跳转首页
                return render(request, "index.html")
            else:
                context = {'msg': '账号或密码错误'}
                return render(request, 'login.html', context=context)
        else:
            context = {'login_form':login_form}
            return render(request, 'login.html', context=context)


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        context = {'register_form':register_form}
        return render(request,"register.html",context)


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
