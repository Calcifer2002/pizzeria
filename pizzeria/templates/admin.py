from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Crust, Size, Sauce, Cheese, Pizza, Topping, Order

admin.site.register(Crust)
admin.site.register(Size)
admin.site.register(Sauce)
admin.site.register(Cheese)
admin.site.register(Pizza)
admin.site.register(Topping)


admin.site.register(Order)