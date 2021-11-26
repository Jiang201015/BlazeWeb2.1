from django.urls import path
from . import views

app_name = 'serviceApp'

urlpatterns = [
    path('download/', views.download, name='download'),  # 资料下载页面
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),#单项资料下载
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
    path('facedetect/', views.facedetect, name='facedetect'),  # 人脸检测api
    path('facedetectDemo/', views.facedetectDemo, name='facedetectDemo'),  # 人脸检测api
]