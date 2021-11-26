from django.urls import path
from . import views

app_name = 'productsApp'

urlpatterns = [
    path('products/<str:productName>/', views.products, name='products'),#产品列表
    path('productDetail/<int:id>/', views.productDetail, name='productDetail'),#产品详情
]