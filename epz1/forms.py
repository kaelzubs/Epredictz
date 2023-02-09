from django.form import forms


class DateInput(forms.DateInput):
    input_type = 'date

class LastActiveForm(forms.Form):
    """
    Last Active Date Form
    """
    last_active = forms.DateField(widget=DateInput)
