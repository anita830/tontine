from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'full_name')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
