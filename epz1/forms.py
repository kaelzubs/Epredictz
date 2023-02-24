from django import forms
from .models import Home_Page


class DateForm(forms.ModelForm):
    model = Home_Page
    fields = ["pub_date"]
    pub_date = forms.DateField(
        input_formats = ['%Y/%m/%d'],
        widget = forms.DateTimeInput(attrs = {
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    ) 
