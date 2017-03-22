from django.db import models


class Organization(models.Model):
    org_name = models.CharField(unique=True, max_length=150)
    rsi_url = models.URLField(unique=True)
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.org_name)
