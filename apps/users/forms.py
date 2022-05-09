from django import  forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True) #我们字段时char类型的,required=True是必填不允许为空，为空则报错
    password = forms.CharField(required=True,min_length=5) #密码的最小长度


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"}) #验证码字段


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)

    captcha = CaptchaField(error_messages={"invalid":"验证码错误"}) #验证码字段


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)