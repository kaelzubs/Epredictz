from django.shortcuts import render
from epz7.forms import EmailSignupForm
# Create your views here.

def list_disclaim(request):
    forms = EmailSignupForm()
    return render(request, 'disclaimer_page.html', {'forms': forms})
