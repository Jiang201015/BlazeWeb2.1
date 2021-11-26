from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('游戏作品', '游戏作品'),
        ('技术作品', '技术作品'),
        ('教程作品', '教程作品'),
    )
    title = models.CharField(max_length=50, verbose_name=' 产品标题')
    description = models.TextField(verbose_name='产品详情描述')
    productType = models.CharField(choices=PRODUCTS_CHOICES,
                                   max_length=50,
                                   verbose_name='产品类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
        ordering = ('-publishDate', )


class ProductImg(models.Model):
    product = models.ForeignKey(Product,
                                related_name='productImgs',
                                verbose_name='产品',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Product/',
                              blank=True,
                              verbose_name='产品图片')

    class Meta:
        verbose_name = '产品图片'
        verbose_name_plural = '产品图片'