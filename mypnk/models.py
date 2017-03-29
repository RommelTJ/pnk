from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.datetime_safe import date


class Organization(models.Model):
    name = models.CharField(unique=True, max_length=150)
    short_name = models.CharField(unique=True, max_length=4, default=None)
    rsi_url = models.URLField(unique=True)
    website_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return '%s' % self.name


class PNKEmployee(models.Model):

    EMPLOYEE_TYPES = (
        ('MEM', 'Member'),
        ('AFF', 'Affiliate'),
        ('RET', 'Retired'),
        ('KIA', 'Killed in action'),
    )

    user = models.ForeignKey(User)
    org = models.ManyToManyField(Organization, related_name='organizations')
    type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default='AFF')
    callsign = models.CharField(max_length=255)
    birth_date = models.DateField(default=timezone.now)
    hire_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    class Meta:
        db_table = 'pnk_employees'
