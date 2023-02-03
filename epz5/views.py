from django.shortcuts import render

# Create your views here.

def list_faqs(request):
    return render(request, 'faq_page.html', {})
