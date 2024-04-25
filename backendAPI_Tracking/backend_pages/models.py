from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Страница')
    published = models.BooleanField(default=False)
    page_link = models.URLField(blank=True)
    qr_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class PageStatistics(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    visits = models.PositiveIntegerField(default=0)
    unique_users = models.PositiveIntegerField(default=0)
    visits_phone = models.PositiveIntegerField(default=0)
    visits_comp = models.PositiveIntegerField(default=0)
    click_links = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Statistics for {self.date}"