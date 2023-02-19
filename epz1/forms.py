from django import forms
from . models import Home_Page


class PickDateForm(forms.Form):
    date_time = forms.DateField(widget=forms.DateInput(attrs={'class': 'any_custom_class_name'}))
    class Meta:
        model = Home_Page
        fields = ['date_time']
