from django.contrib import admin
from .models import Product,ProductImg

class ProductImgInline(admin.StackedInline):
    model = ProductImg
    extra = 1     # 默认显示条目的数量

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline,]

admin.site.register(Product, ProductAdmin)