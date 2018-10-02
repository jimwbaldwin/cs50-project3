from django.contrib import admin

from .models import PizzaCrust, PizzaStyle, PizzaSize
from .models import PizzaTopping, Pizza

# Register your models here.
admin.site.register(PizzaCrust)
admin.site.register(PizzaStyle)
admin.site.register(PizzaSize)
admin.site.register(PizzaTopping)
admin.site.register(Pizza)