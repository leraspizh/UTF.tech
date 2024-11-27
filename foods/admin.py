from django.contrib import admin
from foods.models import FoodCategory, Food


admin.site.register(FoodCategory)
admin.site.register(Food)
