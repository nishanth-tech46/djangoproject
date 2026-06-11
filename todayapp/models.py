from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=10,unique=True)
    course=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name