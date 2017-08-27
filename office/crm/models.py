from django.db import models

# Create your models here.


class Account(models.Model):

    depID = models.IntegerField(primary_key=True)  # 编码
    depName = models.CharField(primary_key=True,max_length=45)  # 名称
    depcompanyID = models.IntegerField()  # 公司编码
    depParentID = models.IntegerField()  # 上级部门编号
    depLogoUrl= models.URLField(max_length=100) # logo存储链接
    depAddress = models.CharField(max_length=100) # 地址
    depSite = models.URLField(max_length=100) # 公司官网
    depCreatAt = models.DateTimeField(default='CURRENT_TIMESTAMP ') # 创建时间
    depFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）


