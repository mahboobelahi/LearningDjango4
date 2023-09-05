from django.db import models

# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars = models.IntegerField()

    def __str__(self):

        return f"({self.first_name},{self.last_name},{self.stars})"