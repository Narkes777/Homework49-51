from django.db import models

# Create your models here.


class Order(models.Model):
    electro = models.ForeignKey('Electronics', on_delete=models.CASCADE)
    cloth = models.ForeignKey('Clothing', on_delete=models.CASCADE)
    books = models.ForeignKey('Books', on_delete=models.CASCADE)


class Electronics(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()



class Clothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()



class Books(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()