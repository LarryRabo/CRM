from django.db import models

# Create your models here.

# 用户表，存放用户登陆信息


class User(models.Model):

    userId = models.AutoField('ID', primary_key=True,name='test',db_index=True)
    userName = models.CharField(max_length=45, unique=True)   # 用户名
    userPassword = models.CharField(max_length=30)  # 密码
    userMobile = models.IntegerField(unique=True)  # 手机
    userEmail = models.IntegerField(unique=True)   # 邮箱
    userType = models.IntegerField(default="0")  # 用户类型（0：普通用户，1：经理级用户，2：管理员用户，3：超级管理员）
    userFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）
    userCreateAt = models.DateTimeField(default='CURRENT_TIMESTAMP ')  # 用户创建时间


# 角色表

class Role(models.Model):

    roleId = models.AutoField('ID', primary_key=True)   # 角色编号
    roleName = models.CharField(max_length=45, unique=True)   # 角色名称
    roleFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）
    roleCreateAt = models.DateTimeField(default='CURRENT_TIMESTAMP ')  # 用户创建时间

# 用户角色表

class RoleUser(models.Model):

    roleToUserID=models.IntegerField(primary_key=True)   # 用户编号
    userToRoleID=models.IntegerField(primary_key=True)   # 用户编号



# 权限表

class Right(models.Model):

    rightCode = models.AutoField('ID', primary_key=True)  # 权限编号
    rightText = models.CharField(max_length=100)  # 权限编号
    rightParentCode = models.IntegerField()   # 父节点编号
    rightType = models.IntegerField(default='0')   # 权限类型（0：操作类，1：显示类）
    rightUrl = models.URLField(max_length=100)   # 权限链接地址
    rightTip = models.IntegerField(default='0')   # 显示

# 角色权限表

class RoleRight(models.Model):

    rfRoleId = models.IntegerField(primary_key=True)  # 角色编码
    rfRightCode = models.IntegerField(primary_key=True)  # 权限编号
    rfFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）

# 公司信息表

class Company(models.Model):

    companyID = models.IntegerField(primary_key=True)  # 编码
    companyName = models.IntegerField(primary_key=True)  # 公司名称
    companyLogoUrl = models.URLField(max_length=100)  # 公司logo存储链接
    companyAddress = models.CharField(max_length=100)  # 地址
    companySite = models.URLField(max_length=100)  # 公司官网
    companyCreatAt = models.DateTimeField(default='CURRENT_TIMESTAMP ')  # 添加公司时间
    companyFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）

# 部门表

class Department(models.Model):

    depID = models.IntegerField(primary_key=True)  # 编码
    depName = models.CharField(max_length=45,primary_key=True)  # 名称
    depCompanyID = models.IntegerField(primary_key=True)  # 公司编码
    depParentID = models.IntegerField(primary_key=True)  # 上级部门编号
    depLogoUrl= models.URLField(max_length=100)  # logo存储链接
    depAddress = models.CharField(max_length=100)  # 地址
    depSite = models.URLField(max_length=100)  # 公司官网
    depCreatAt = models.DateTimeField(default='CURRENT_TIMESTAMP ')  # 创建时间
    depFlag = models.IntegerField(default="1")  # 状态（0：已经删除，1：未删除）

