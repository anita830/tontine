from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=255)
    entity_id = models.PositiveIntegerField()
    before_json = models.JSONField(null=True, blank=True)
    after_json = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.actor} - {self.action} on {self.entity_type}:{self.entity_id}'
