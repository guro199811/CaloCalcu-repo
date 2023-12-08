from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

class Drink(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()