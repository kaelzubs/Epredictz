from django_flatpickr.widgets import DatePickerInput
from .models import Home_Page
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Home_Page
        fields = "__all__"
        widgets = {
            "pub_date": DatePickerInput(),
        }
