from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'device_type', 'status', 'created_at']
    list_filter = ['device_type', 'status']
    search_fields = ['name']