from django.db import models
from django.conf import settings
from apps.groups.models import Group
from apps.cycles.models import Cycle

class Payout(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PAID = 'PAID', 'Paid'

    cycle = models.OneToOneField(Cycle, on_delete=models.CASCADE, related_name='payout')
    beneficiary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payouts')
    amount_paid_out = models.DecimalField(max_digits=12, decimal_places=2)
    payout_date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    proof_reference = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Payout for {self.beneficiary} in {self.cycle}'
