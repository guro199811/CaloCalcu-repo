from django.db import models
from django.contrib.auth.models import User


#user-specific details like age, weight, height, and possibly fitness goals.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in kilograms
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in centimeters

#name, calories per serving, serving size, category (e.g., protein, carbs, fats).
class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

class Drink(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

#user (foreign key to User model), date, time, notes.
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

#This model will represent the foods that a user consumes in a specific meal.
class ConsumedFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class ConsumedDrink(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


#This model could help in tracking a user's daily calorie intake.
class DailyCalorieIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    total_calories_consumed = models.PositiveIntegerField()
