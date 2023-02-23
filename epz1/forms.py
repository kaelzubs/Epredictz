from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from .models import Home_Page


class DateEventForm(forms.ModelForm):
    class Meta:
        model = Home_Page
        fields = ["start_date", "start_time", "start_datetime", "start_month", "start_year"]
        widgets = {
            "start_date": DatePickerInput(),
            "start_time": TimePickerInput(),
            "start_datetime": DateTimePickerInput(),
            "start_month": MonthPickerInput(),
            "start_year": YearPickerInput(),
        }
