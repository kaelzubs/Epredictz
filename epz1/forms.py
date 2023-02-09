from django.form import forms
from .models import Home_Page


class DateInput(forms.DateInput):
    input_type = 'date

class LastActiveForm(forms.Form):
    """
    Last Active Date Form
    """
    pub_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Home_Page
        fields = ('email',)
