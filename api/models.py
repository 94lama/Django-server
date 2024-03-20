from django.db import models
from django.utils import timezone

# Create your models here.
class Time(models.Model):
    def __str__(self):
        return self.api_text
    def get_time():
        return timezone.now().strftime("%d-%m-%Y %H:%M:%S")