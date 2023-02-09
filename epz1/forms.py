from django import forms
from .models import Home_Page


class DateInput(forms.DateInput):
    input_type = 'date

class LastActiveForm(forms.Form):
    date_added = forms.DateField(widget=DateInput)
    class Meta:
        model = Home_Page
        fields = ('pub_date')
