from django.db import models

# Create your models here.

class todoTasks(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.CharField(max_length=500)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=False)
    isCompleted = models.BooleanField()