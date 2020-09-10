from django.contrib import admin
from food_list_db.database import models

# Register your models here.
admin.site.register(models.FoodCoding)
admin.site.register(models.BNSFoodCoding)
admin.site.register(models.Category)
admin.site.register(models.FoodItem)
