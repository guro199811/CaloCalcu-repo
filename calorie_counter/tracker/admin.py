from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Meal)
admin.site.register(ConsumedFood)
admin.site.register(ConsumedDrink)
admin.site.register(DailyCalorieIntake)
