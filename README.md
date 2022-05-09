# Django-MxOnline

尝试用Django3写一个内容比较全的 ”慕学在线网“

# 开发环境

操作系统：macOs Monterey 12.3.1

**Python**：3.7.3

**Django**：3.2

**后台**：https://simpleui.88cto.com/simpleui/

# 前言

目前应该算是初学Django，来写的这个项目为了巩固Django，代码写的属实是不优雅，等以后可能会回头完善一下这个项目，再加上我们上课老师在教Git 所以先把这个项目挂到GitHub（虽然还没有写完吧）。

# 相关依赖

## MySQL

Django链接MySQL的时候会出现一些问题，解决如下：

```bash
# 确保 pip 是最新版本
$ pip3 install --upgrade pip
#只支持Python2.7-3.2
$ pip3 install mysql-python
#我们高版本就用mysqlclient来代替了
$ pip3 install mysqlclient
```

## django-simple-captcha

验证码

```bash
$ python3 -m pip install django-simple-captcha==0.5.13
```

这个版本一定要和我们本地的Python版本对应

具体看下 使用文档 https://django-simple-captcha.readthedocs.io/en/latest/usage.html

## simpleui

**项目地址**：https://github.com/sea-team/simpleui

```bash
$ pip3 install django-simpleui
```



# 前台展示

写了一部分并没有写完，完成以后在提交

# 后台展示

写了一部分并没有写完，完成以后在提交