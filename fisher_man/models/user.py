from django.db import models

class User(models.Model):
    USER_TYPES = (
        ('Fisherman', 'Fisherman'),
        ('ADMIN', 'ADMIN'),
    )

    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=10,choices=USER_TYPES,null=True,blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=5,null=True,blank=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=5,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name if self.name else "User"
