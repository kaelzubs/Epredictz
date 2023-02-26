from django.shortcuts import render
from epz7.forms import EmailSignupForm
# Create your views here.

def list_about(request):
    forms = EmailSignupForm()
    return render(request, 'about_page.html', {
        'forms': forms
    })
