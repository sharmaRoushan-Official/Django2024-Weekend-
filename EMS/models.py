from django.db import models

# Create your models here.

class Employee(models.Model):
    id= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=11)
    salary = models.DecimalField(max_digits=18,decimal_places=2)  # 10.23

    def __str__(self):
        return self.name
    
    