from django.db import models
from django.utils.timezone import now

class IPAccess(models.Model):
    ip_address = models.CharField(max_length=255, primary_key=True, default='0.0.0.0')    # Поле для IP-адреса
    expiration_date = models.DateField()  # Дата окончания доступа

    class Meta:
        db_table = 'ip_access'

    def __str__(self):
        return f"{self.ip_address} - {self.expiration_date}"
