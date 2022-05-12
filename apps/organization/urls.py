from organization import views
from django.urls import path,re_path




urlpatterns = [
    re_path(r'^org_list/$',views.OrgView.as_view(),name="org_list"),
]
