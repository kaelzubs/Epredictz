from django.shortcuts import render
from epz7.forms import EmailSignupForm
# Create your views here.

def list_faqs(request):
    forms = EmailSignupForm()
    return render(request, 'faq_page.html', {'forms': forms})
