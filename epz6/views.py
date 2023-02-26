from django.shortcuts import render
from epz7.forms import EmailSignupForm
# Create your views here.

def cookie_policy(request):
    forms = EmailSignupForm()
    return render(request, 'cookielaw/cookie_page.html', {'forms': forms})
