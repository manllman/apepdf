from django.db import models

# 导入django自带的用户模块
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

class Category(models.Model):
    name = models.CharField('分类',max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField('标签', max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tui(models.Model):
    name = models.CharField('推荐位',max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Pdf(models.Model):
    get_code = models.CharField("提取码", max_length=20,null=True)
    name = models.CharField('名称',max_length = 70)
    body = UEditorField('简介', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    img = models.ImageField(upload_to='pdf_img/%Y/%m/%d/', verbose_name='PDF图片', blank=True, null=True)
    down_url = models.CharField('下载地址',max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类',default = '1')
    tags = models.ManyToManyField(Tags,blank=True,verbose_name="标签")


    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    author = models.CharField('作者', max_length=70)
    # pdf的上传者
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="上传者")
    views = models.PositiveIntegerField('浏览量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    get_code = models.CharField("提取码", max_length=20)
    class Meta:
        verbose_name = 'PDF'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.name

# Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接到', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


