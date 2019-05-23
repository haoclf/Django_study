from django.db import models
from backend.common.models import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.


class userProfile(AbstractUser,BaseModel):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=6, choices=(("male",u"男性"),("femal",u"女性")),default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    email = models.EmailField(max_length=100,null=True, blank=True, verbose_name="邮箱")

    class Meta(AbstractUser.Meta):
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = 'userprofile'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class aplDatabase(BaseModel):
    dbtype = models.CharField(max_length=20, blank=False, verbose_name="数据库类型")
    dbstructure = models.CharField(max_length=10, blank=False, verbose_name="数据库架构")
    dbname = models.CharField(max_length=10, blank=False, verbose_name="数据库名")
    username = models.CharField(max_length=64, blank=False, verbose_name="用户名")
    shandow = models.CharField(max_length=64, blank=False, verbose_name="密码")
    cm = models.CharField(max_length=10, blank=False, verbose_name="CPU/Mem")
    disksize = models.CharField(max_length=10, blank=False, verbose_name="磁盘容量")
    note = models.CharField(max_length=128, blank=False, verbose_name="备注")

    class Meta():
        verbose_name = "数据库申请"
        verbose_name_plural = verbose_name
        db_table = "aplDatabase"

    def __str__(self):
        if self.dbname:
            return self.dbname
        else:
            return self.dbtype

class celeryt(BaseModel):
    dbtype = models.CharField(max_length=20, blank=False, verbose_name="数据库类型")
    dbstructure = models.CharField(max_length=10, blank=False, verbose_name="数据库架构")
    dbname = models.CharField(max_length=10, blank=False, verbose_name="数据库名")
    username = models.CharField(max_length=64, blank=False, verbose_name="用户名")
    shandow = models.CharField(max_length=64, blank=False, verbose_name="密码")
    cm = models.CharField(max_length=10, blank=False, verbose_name="CPU/Mem")
    disksize = models.CharField(max_length=10, blank=False, verbose_name="磁盘容量")
    note = models.CharField(max_length=128, blank=False, verbose_name="备注")

    class Meta():
        verbose_name = "数据库申请celerytask"
        verbose_name_plural = verbose_name
        db_table = "celeryt"

    def __str__(self):
        if self.dbname:
            return self.dbname
        else:
            return self.dbtype
