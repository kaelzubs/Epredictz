from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from .models import Home_Page


class DateEventForm(forms.ModelForm):
    class Meta:
        model = Home_Page
        fields = ["pub_date"]
        widgets = {
            "pub_date": DatePickerInput(),
        }
