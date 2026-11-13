from django.db import models

# Create your models here
class Patient(models.Model):

    patient id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email= models.CharField()
    address = models.TextField()
    
    def __str__(self):
        return self.name