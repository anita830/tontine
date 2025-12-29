from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from apps.groups.models import Group
from apps.cycles.models import Cycle

class Contribution(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', 'Cash'
        MOMO = 'MOMO', 'Mobile Money'
        BANK = 'BANK', 'Bank Transfer'

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        VERIFIED = 'VERIFIED', 'Verified'
        REJECTED = 'REJECTED', 'Rejected'

    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='contributions')
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributions')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices, default=PaymentMethod.CASH)
    reference_code = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_contributions')
    verified_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure the member belongs to the group
        if not self.cycle.group.members.filter(user=self.member).exists():
            raise ValidationError("Member is not part of the specified group.")

        settings = self.cycle.group.settings
        if not settings.allow_partial_payment:
            # Check if a contribution already exists for this member in this cycle
            if Contribution.objects.filter(cycle=self.cycle, member=self.member).exclude(pk=self.pk).exists():
                raise ValidationError("A contribution for this member already exists in this cycle.")
            # Check if the amount paid is equal to the contribution amount
            if self.amount_paid != settings.contribution_amount:
                raise ValidationError(f"Amount must be equal to {settings.contribution_amount}.")
        else:
            # Check if the sum of contributions exceeds the expected amount
            total_contributed = Contribution.objects.filter(cycle=self.cycle, member=self.member).exclude(pk=self.pk).aggregate(models.Sum('amount_paid'))['amount_paid__sum'] or 0
            if total_contributed + self.amount_paid > settings.contribution_amount:
                raise ValidationError(f"Total contribution for this cycle cannot exceed {settings.contribution_amount}.")

    def __str__(self):
        return f'Contribution from {self.member} for {self.cycle}'
