from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )

    name = models.CharField(max_length=100,verbose_name='名字')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否置顶')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除')
    )
    name = models.CharField(max_length=100,verbose_name='名字')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
        (STATUS_DRAFT,'草稿')
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    content = models.TextField(verbose_name='content',help_text='格式必须是MarkDown ')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    desc = models.CharField(max_length=1024,verbose_name='概述')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL,verbose_name='状态')
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING, blank=True, null=True,verbose_name='分类')
    tags = models.ManyToManyField(Tag,blank=True, null=True,verbose_name='标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True,verbose_name='更新时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title
