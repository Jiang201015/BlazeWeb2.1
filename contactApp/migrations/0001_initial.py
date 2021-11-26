# Generated by Django 2.2.4 on 2021-11-24 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='招聘岗位')),
                ('description', models.TextField(verbose_name='岗位要求')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '招聘广告',
                'verbose_name_plural': '招聘广告',
                'ordering': ('-publishDate',),
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('personID', models.CharField(max_length=30, verbose_name='社区ID网址')),
                ('sex', models.CharField(default='男', max_length=5, verbose_name='性别')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱(没有写无)')),
                ('birth', models.DateField(default='2021-11-24', max_length=20, verbose_name='出生日期')),
                ('edu', models.CharField(default='小学', max_length=5, verbose_name='学历')),
                ('position', models.CharField(max_length=40, verbose_name='申请职位')),
                ('experience', models.TextField(blank=True, null=True, verbose_name='学习或工作经历')),
                ('photo', models.ImageField(upload_to='contact/recruit/%Y_%m_%d', verbose_name='头像照片')),
                ('status', models.IntegerField(choices=[(1, '未审'), (2, '通过'), (3, '未通过')], default=1, verbose_name='面试成绩')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='提交时间')),
            ],
            options={
                'verbose_name': '简历',
                'verbose_name_plural': '简历',
                'ordering': ('-status', '-publishDate'),
            },
        ),
    ]
