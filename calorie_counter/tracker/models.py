from django.db import models

# Models for Database

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

class Drink(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()