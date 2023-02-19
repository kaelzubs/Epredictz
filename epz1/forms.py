from django import forms


class PickDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'any_custom_class_name'}))
