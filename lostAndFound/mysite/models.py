from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 用户(User)模型
# 采用的继承方式扩展用户信息
class User(AbstractUser):
    # 在继承的基础上新增4个字段
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True,
                               null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    wx = models.CharField(max_length=20,blank=True,null=True,verbose_name='微信')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    # 使用内部的class Meta 定义模型的元数据
    class Meta:
        # verbose_name：数据库表名名称，这里表名称为“用户”
        verbose_name = '用户'
        # verbose_name_plural：人类可读的单复数名称，这里“用户”复数名称为“用户”
        verbose_name_plural = verbose_name
        # ordering：如排序选项，这里以id降序来排序
        ordering = ['-id']

    # 对象的字符串表达式(unicode格式)
    def __str__(self):
        return self.username

# 文章(Article)模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    desc = models.CharField(max_length=50, verbose_name="文章描述")
    content = models.TextField(verbose_name='文章内容')
    # 拾得物品OR寻找物品
    type = models.BooleanField(default=0, verbose_name="发布类型")
    is_founded = models.BooleanField(default=0, verbose_name="是否找到")
    position = models.CharField(max_length=100, verbose_name="可能出现的位置")
    photo = models.ImageField(upload_to='/articleImg', verbose_name="图片路径")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title


# 评论(comment)模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户',  on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章',  on_delete=models.CASCADE)
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论',  on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.content)