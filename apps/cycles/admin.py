from django.contrib import admin
from .models import Cycle

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('group', 'cycle_number', 'beneficiary', 'start_date', 'end_date', 'status', 'expected_total')
    list_filter = ('group', 'status')
    search_fields = ('group__name', 'beneficiary__full_name')
    ordering = ('-start_date',)
