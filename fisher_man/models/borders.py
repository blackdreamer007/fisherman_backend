from django.db import models

class Border(models.Model):
    id = models.BigAutoField(primary_key=True)
    border_name = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        db_table = 'borders'

    def __str__(self):
        return self.border_name if self.border_name else "Border"