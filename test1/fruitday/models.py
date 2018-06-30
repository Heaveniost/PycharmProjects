from django.db import models


# class Publish(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     country = models.CharField(max_length=50)
#     website = models.URLField()

class Users(models.Model):
    uphone = models.CharField(max_length=20)
    upswd = models.CharField(max_length=50)
    uemail = models.EmailField()
    uname = models.CharField(max_length=20,null=True)
    isActivate = models.BooleanField(default=True)