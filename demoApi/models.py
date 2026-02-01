from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name
    


