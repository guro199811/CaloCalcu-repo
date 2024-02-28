from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    api_id = models.CharField(max_length=255, unique=True)
    nutritional_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class FoodHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_list = ArrayField(models.IntegerField())
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.user.username} - ({self.date_added})"
    
