from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    user_email=models.CharField(max_length=45)
    user_mobile=models.CharField(max_length=45)

    def __unicode__(self):
        return self.user_name