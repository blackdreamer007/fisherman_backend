from django.db import models
from fisher_man.models.user import User

class FishPotentials(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="user_id"
    )
    fish_name = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
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
        db_table = 'fish_potentials'

    def __str__(self):
        return f"FishPotential {self.id}"
