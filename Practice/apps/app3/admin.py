from django.contrib import admin
from apps.app3.models import Images

# Register your models here.
@admin.register(Images)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    