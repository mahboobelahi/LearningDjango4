from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Car(models.Model):
    #pk
    brand = models.CharField(max_length=30)
    year =  models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand}, {self.year}"