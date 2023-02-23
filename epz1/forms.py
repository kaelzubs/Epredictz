from django_flatpickr.widgets import DatePickerInput
from .models import Home_Page
from django import forms


class DateEventForm(forms.ModelForm):
    class Meta:
        model = Home_Page
        fields = ["pub_date"]
        widgets = {
            "pub_date": DatePickerInput(),
        }
