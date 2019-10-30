from django.contrib import admin

# Register your models here.


#jx
from .models import Menu, Item

#admin.site.register(Question, QuestionAdmin)
admin.site.register(Menu)

admin.site.register(Item)


