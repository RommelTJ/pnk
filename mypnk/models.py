from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Organization(models.Model):
    org_name = models.CharField(unique=True, max_length=150)
    org_short_name = models.CharField(unique=True, max_length=4, default=None)
    rsi_url = models.URLField(unique=True)
    website_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return '%s' % (self.org_name)


class PNKEmployee(models.Model):
    user = models.ForeignKey(User)
    org = models.ManyToManyField(Organization)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
