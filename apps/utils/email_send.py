from users.models import EmailVerifyRecord
from django.core.mail import send_mail

from random import Random
from MxOnline.settings import EMAIL_FROM




#生成随机字符
def random_str(randomlength=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

#邮箱验证码保存到数据库
def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16) #生成随机字符串
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_boby = ""

    if send_type == "register":
        email_title = "慕学在线网注册机激活链接"
        email_boby = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title,email_boby,EMAIL_FROM,[email])
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "慕学在线网密码重置链接"
        email_boby = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email]) #发送邮件
        if send_status:
            pass





