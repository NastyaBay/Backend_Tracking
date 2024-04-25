from django.db import models
from django.conf import settings

# Create your models here.
class UserStatistics(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, blank=True)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    number_visits = models.IntegerField(default=0)
    number_forms = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

