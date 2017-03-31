import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.utils.datetime_safe import datetime
from stdimage import StdImageField
from django.conf import settings


class LocalFileSystemStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if os.path.exists(self.path(name)):
            # Check if the thumbnail is also removed
            os.remove(self.path(name))
        return name

fs = LocalFileSystemStorage()


class Organization(models.Model):
    name = models.CharField(unique=True, max_length=150)
    short_name = models.CharField(unique=True, max_length=4, default=None)
    rsi_url = models.URLField(unique=True)
    website_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return '%s' % self.name


def upload_path_handler(self, filename):
    return u'profile/user_{id}/{file}'.format(id=self.pk, file=filename)


def generate_next_emp_no():
    return 1 if PNKEmployee.objects.all().count() == 0 else PNKEmployee.objects.all().aggregate(Max('emp_no'))['emp_no__max'] + 1


class PNKEmployee(models.Model):

    EMPLOYEE_TYPES = (
        ('MEM', 'Member'),
        ('AFF', 'Affiliate'),
        ('RET', 'Retired'),
        ('KIA', 'Killed in action'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.IntegerField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    org = models.ManyToManyField(Organization, related_name='organizations')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default='AFF')
    callsign = models.CharField(max_length=255)
    birth_date = models.DateField(default=datetime(1980, 01, 01))
    hire_date = models.DateTimeField(default=timezone.now, blank=True)
    image = StdImageField(upload_to=upload_path_handler, storage=fs, null=True, blank=True, max_length=255, variations={
        'large': (528, 750),
        'thumbnail': (88,125, True),
        'medium': (264, 375),
    })

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    class Meta:
        db_table = 'pnk_employees'
