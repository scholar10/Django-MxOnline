from users import views
from django.urls import path,re_path


urlpatterns = [

    re_path(r'^login/$',views.LoginView.as_view(),name="login"),
    re_path(r'^register/$',views.RegisterView.as_view(),name="register"),
    re_path(r'^active/(?P<active_code>.*)/$',views.ActiveUserView.as_view(),name="user_active"),

    re_path(r'^forget/$',views.ForgetPwdView.as_view(),name="forget_pwd"),
    re_path(r'^reset/(?P<active_code>.*)/$',views.RestView.as_view(),name="reset_pwd"),
    re_path(r'^modify_pwd/$',views.ModifyPwdView.as_view(),name="modify_pwd"),

]