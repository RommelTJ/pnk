from django import forms
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.safestring import mark_safe
from registration.forms import RegistrationForm
from registration.signals import user_registered
from django_countries.widgets import CountrySelectWidget

from .models import PNKEmployee, generate_next_emp_no, Organization


class AdminImageFieldWidget(forms.widgets.FileInput):
    def __init__(self, placeholder='/media/profile/placeholder.thumbnail.png'):
        self.placeholder = placeholder
        super(AdminImageFieldWidget, self).__init__({})

    def render(self, name, image, attrs=None):
        render_html = '<img src="%s" />' % (image.thumbnail.url) if image and hasattr(image, "url") else '<img src="%s" />' % (self.placeholder)
        return mark_safe("%s%s" % (render_html, super(AdminImageFieldWidget, self).render(name, image, attrs)))


class PNKEmployeeForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, 2025)), initial=datetime(1988, 01, 01))
    image = forms.ImageField(label='Profile Image', widget=AdminImageFieldWidget(), required=False)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        model = PNKEmployee
        fields = ('callsign', 'rsi_url', 'org', 'country', 'gender', 'birth_date', 'image')
        widgets = {'country': CountrySelectWidget()}


class MyExtendedForm(RegistrationForm):
    """
    Extends the base registration form to include first name and last name
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Chris'}),
        required=True,
        label='First name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Roberts'}),
        required=True,
        label='Last name'
    )


def user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form = MyExtendedForm(request.POST)
    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()


user_registered.connect(user_created)
