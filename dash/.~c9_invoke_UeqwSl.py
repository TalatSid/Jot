from django.db import models


# Create your models here.
class Task(models.Model):
    task_desc = models.CharField(max_length = 250)
    tasktyp = models.CharField(max_length = 10)
    estimate = models.DecimalField(decimal_places = 2,max_digits = 6)
    spent = models.DecimalField(decimal_places = 2,max_digits = 6)
    owner = models.CharField(max_length = 50)
    email = models.EmailField()
    sprint = models.CharField(max_length = 10)
    status = models.CharField(max_length = 15)

     def __str__(self):
         return f"{self.item} ({self.cost})"