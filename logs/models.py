from django.db import models

class Log(models.Model):
    ip_address = models.CharField(max_length=100, blank=True)
    access_time = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "logs"
