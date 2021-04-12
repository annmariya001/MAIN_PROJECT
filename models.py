from django.db import models
class Userreg(models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=30)
     address = models.CharField(max_length=30)
     uname= models.CharField(max_length=30)
class Login(models.Model):
     uname = models.CharField(max_length=30)
     password = models.CharField(max_length=30)
     status = models.IntegerField()
class Addfood(models.Model):
     food = models.CharField(max_length=30)
     price = models.CharField(max_length=30)
     description = models.CharField(max_length=30)
     category = models.CharField(max_length=30)
class Addfoodcategories(models.Model):
     name = models.CharField(max_length=30)

