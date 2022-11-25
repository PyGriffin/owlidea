from django.db import models
from django.contrib.auth.models import User


class Sidebar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0

    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
        )
    SIDE_TYPE = (
        (1,'HTML'),
        (2,'最新文章'),
        (3,'最热文章'),
        (4,'近期文章'),
    )

    title = models.CharField(max_length=100,verbose_name='标题')
    display_type = models.PositiveIntegerField(choices=SIDE_TYPE,default=1,verbose_name='展示类型')
    content = models.CharField(max_length=500,verbose_name='内容',blank=True,help_text='如果设置的不是HTML 可为空')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS,default=STATUS_SHOW,verbose_name='状态')
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING, blank=True, null=True,verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'

    def __str__(self):
        return self.title


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE,'删除'),
        )

    title = models.CharField(max_length=100,verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.IntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='状态')
    weight = models.PositiveIntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name='权重',help_text='权重高展示靠前')
    owner = models.ForeignKey(User,on_delete=models.DateTimeField,verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = 'link'

    def __str__(self):
        return self.title

