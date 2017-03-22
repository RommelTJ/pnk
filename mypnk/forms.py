from django import forms
from .models import PNKEmployee


class PNKEmployeeForm(forms.ModelForm):

    class Meta:
        model = PNKEmployee
        fields = '__all__'
