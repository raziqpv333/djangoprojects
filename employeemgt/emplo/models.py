from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    jod=models.TextField()
    salary=models.IntegerField()

