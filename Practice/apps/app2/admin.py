from django.contrib import admin

# Register your models here.
from apps.app2.Models.models import Employee

@admin.register(Employee)
class EmployeeDisplay(admin.ModelAdmin):
    list_display = ('name','email','salary','is_active')
    list_filter = ('gender','is_active','date_joined')
    search_fields = ('name','email')
    list_editable = ('is_active',)