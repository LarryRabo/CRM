from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    useremail=models.CharField(max_length=45)
    usermobile=models.CharField(max_length=45)

    def __unicode__(self):
        return self.username