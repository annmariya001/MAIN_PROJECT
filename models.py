from django.db import models
class Userreg(models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     phone = models.CharField(max_length=30)
     address = models.CharField(max_length=30)
     username= models.CharField(max_length=30)
class Login(models.Model):
     username = models.CharField(max_length=30)
     password = models.CharField(max_length=30)
     status = models.IntegerField()
class Addfood(models.Model):
     food = models.CharField(max_length=30)
     price = models.CharField(max_length=30)
     description = models.CharField(max_length=30)
     category = models.CharField(max_length=30)
     photo= models.FileField()
class Addfoodcategories(models.Model):
     name = models.CharField(max_length=30)
class Addchef(models.Model):
     name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     designation = models.CharField(max_length=30)
     photo = models.FileField(max_length=30)
class Tableset(models.Model):
     tablename = models.CharField(max_length=30)
     tablesize = models.CharField(max_length=30)
class Tablereservation(models.Model):
     guest = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     username = models.CharField(max_length=30)
     date = models.CharField(max_length=30)
     time = models.CharField(max_length=30)

