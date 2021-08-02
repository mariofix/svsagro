from django.contrib import admin
from .models import Customer, Machine


class CustomerFilters(admin.ModelAdmin):
    model = Customer
    list_display = ["name", "country"]


class MachineFilters(admin.ModelAdmin):
    model = Machine
    list_display = ["number", "type", "customer"]


admin.site.register(Customer, CustomerFilters)
admin.site.register(Machine, MachineFilters)
