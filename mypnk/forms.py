from django import forms
from .models import PNKEmployee


class PNKEmployeeForm(forms.ModelForm):

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        model = PNKEmployee
        fields = '__all__'
