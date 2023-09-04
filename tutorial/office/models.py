from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    heart_rate = models.IntegerField(default=60, validators=[MinValueValidator(1),MaxValueValidator(300)])

    #*display object info during query
    def __str__(self) :
        return f"({self.last_name},{self.first_name},{self.age},{self.heart_rate})"