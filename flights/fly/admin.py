from django.contrib import admin
from .models import fly, category, Ticket,Passenger

# Register your models here.

admin.site.register(fly)
admin.site.register(category)
admin.site.register(Ticket)
admin.site.register(Passenger)
