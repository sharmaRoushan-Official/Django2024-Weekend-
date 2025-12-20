from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) # it is mandatory fileld (*) mark
    age = models.IntegerField()
    mobileNo = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True) # it is not a mandatory field
    pic = models.ImageField(null=True, blank=True)  # you've need to install pillow for images otherwise it throw an error.
    created_date = models.DateTimeField(auto_now_add=True)
    last_Modified_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

class paymentDetails(models.Model):
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=100, choices=[("Cash","Cash"),('Debit Card',"Debit Card"),('PayTM',"PayTM"),("Credit Card","Credit Card")])
    payment_date = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(student,null=False, blank=False, on_delete=models.CASCADE) # Student is a variable but variable must be same as relationship database name [student] but in alwasy smallcase.

#model class Course [create relationsip with student]
class Course(models.Model):
    name = models.CharField(max_length=100)

    student = models.ManyToManyField(student,null=True,blank=True)

    def __str__(self):
        return self.name

