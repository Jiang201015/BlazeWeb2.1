"""BlazeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from homeApp.views import home,page_not_found,server_error
from django.views.generic.base import RedirectView
from django.views.static import serve
from django import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                    # 管理员
    path('', home, name='home'),                        # 首页
    path('aboutApp/', include('aboutApp.urls')),        # 公司简介
    path('contactApp/', include('contactApp.urls')),    # 人才招聘
    path('newsApp/', include('newsApp.urls')),          # 新闻动态
    path('productsApp/', include('productsApp.urls')),  # 产品中心
    path('scienceApp/', include('scienceApp.urls')),    # 科研基地
    path('serviceApp/', include('serviceApp.urls')),    # 服务支持
    path('ueditor/',include('DjangoUeditor.urls' )),    # 富文本应用
    path('search/', include('haystack.urls')),          # 搜索应用 
    url(r'^favicon\.ico$',RedirectView.as_view(url=r'static/img/favicon.ico')),    #网页图标 
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
handler500 = server_error