from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    place=models.TextField()
    def __str__(self):
        return self.name+'-'+self.place

class employee(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    position=models.TextField()
    