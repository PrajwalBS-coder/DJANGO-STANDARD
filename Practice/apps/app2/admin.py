from django.contrib import admin

# Register your models here.
from apps.app2.Models.models import Employee,ImageModel

@admin.register(Employee)
class EmployeeDisplay(admin.ModelAdmin):
    list_display = ('name','email','salary','is_active')
    list_filter = ('gender','is_active','date_joined')
    search_fields = ('name','email')
    list_editable = ('is_active',)

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'uploaded_at','image')
    search_fields = ('description',)
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)