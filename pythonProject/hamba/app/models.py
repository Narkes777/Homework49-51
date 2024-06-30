from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Announcement(models.Model):
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)




class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)



class Comentary(models.Model):
    comment = models.TextField()
    ann = models.ForeignKey(Announcement, on_delete=models.CASCADE)


class hjjg(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)