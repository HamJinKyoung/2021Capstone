from django.contrib import admin
from .models import CustomUser, Menu, Basket, Pay

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Menu)
admin.site.register(Basket)
admin.site.register(Pay)
