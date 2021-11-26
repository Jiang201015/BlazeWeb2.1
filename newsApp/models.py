from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.


class MyNew(models.Model):
    NEWS_CHOICES = (
        ('工作室要闻', '工作室要闻'),
        ('行业新闻', '行业新闻'),
        ('通知公告', '通知公告'),
    )
    title = models.CharField(max_length=50, verbose_name=' 新闻标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='news/images/',
                               filePath='news/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='新闻类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)
    photo = models.ImageField(upload_to='news/',
                              blank=True,
                              null=True,
                              verbose_name='展报')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "新闻"
        verbose_name_plural = verbose_name