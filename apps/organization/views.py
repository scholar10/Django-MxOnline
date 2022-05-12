from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class OrgView(View):
    """
        课程机构列表功能
    """
    def get(self,request):
        all_orgs = CourseOrg.objects.all() #取所有课程机构数据
        all_city = CityDict.objects.all() #取所有的城市
        hot_orgs = all_orgs.order_by("-click_num")[:3] #根据点击量(click_num)提取热门机构，倒序排名 取3个最热门机构

        #取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id :
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #取出刷选类别
        category = request.GET.get('ct',"")
        if category:
            all_orgs = all_orgs.filter(category=category)

        #排序
        sort = request.GET.get('sort',"")
        if sort:
            #根据学生人数排序
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            #根据课程数排序
            elif sort == "course_num":
                all_orgs = all_orgs.order_by("-course_num")

        #统计机构一共有多少个
        org_nums = all_orgs.count()
        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 5,request=request)

        orgs = p.page(page) #自动进行分页

        context = {"all_orgs":orgs,"all_city":all_city,"org_nums":org_nums,"city_id":city_id,"category":category,"hot_orgs":hot_orgs,"sort":sort}
        return render(request,"org-list.html",context=context)