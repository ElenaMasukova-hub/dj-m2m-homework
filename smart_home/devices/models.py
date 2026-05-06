from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)  # lamp, sensor, etc.
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.device_type})"