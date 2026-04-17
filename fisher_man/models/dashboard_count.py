from django.db import models

class DashboardCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    borders = models.IntegerField(null=True, blank=True)
    border_crossed = models.IntegerField(null=True, blank=True)
    fishing_zones = models.IntegerField(null=True, blank=True)
    emergencies = models.IntegerField(null=True, blank=True)
    fishermans = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'dashboard_count'

    def __str__(self):
        return f"DashboardCount {self.id}"
