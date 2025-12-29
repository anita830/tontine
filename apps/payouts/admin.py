from django.contrib import admin
from .models import Payout

@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ('cycle', 'beneficiary', 'amount_paid_out', 'payout_date', 'status')
    list_filter = ('cycle__group', 'status')
    search_fields = ('beneficiary__full_name', 'cycle__group__name')
    ordering = ('-payout_date',)
