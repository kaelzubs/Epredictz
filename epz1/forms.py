from django import forms
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
        fields = ('date_tme', 'league','home_team', 'away_team', 'tip', 'tip_odd', 'result', 'slug', 'pub_date')
