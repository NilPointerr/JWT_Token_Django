from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    def __str__(self):
        return self.name