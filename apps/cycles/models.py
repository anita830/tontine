from django.db import models
from django.conf import settings
from apps.groups.models import Group

class Cycle(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        CLOSED = 'CLOSED', 'Closed'

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='cycles')
    cycle_number = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    beneficiary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='beneficiary_cycles')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    expected_total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'cycle_number')
        ordering = ['-cycle_number']

    def save(self, *args, **kwargs):
        if not self.pk:  # Only calculate on creation
            active_members = self.group.members.filter(status='ACTIVE').count()
            self.expected_total = self.group.settings.contribution_amount * active_members
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.group.name} - Cycle {self.cycle_number}'
