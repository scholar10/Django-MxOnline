from users import views
from django.urls import path,re_path


urlpatterns = [

    re_path(r'^login/$',views.LoginView.as_view(),name="login"),
    re_path(r'^register/$',views.RegisterView.as_view(),name="register"),

]