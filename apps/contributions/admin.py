from django.contrib import admin
from .models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('cycle', 'member', 'amount_paid', 'payment_date', 'status')
    list_filter = ('cycle__group', 'cycle', 'status', 'payment_method')
    search_fields = ('member__full_name', 'cycle__group__name')
    ordering = ('-payment_date',)
