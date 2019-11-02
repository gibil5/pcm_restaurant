from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Family)

admin.site.register(MainCourse)

admin.site.register(Dessert)

admin.site.register(Entry)

admin.site.register(Drink)

admin.site.register(HotDrink)
