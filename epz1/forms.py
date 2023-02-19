from django import forms
from django.forms import ModelForm

from .models import Home_Page


class DateInput(forms.DateInput):
    input_type = 'date'


class SeaechForm(ModelForm):

    class Meta:
        model = Home_Page
        fields = ['date_time']
        widgets = {
            'date_time': DateInput(),
        }
