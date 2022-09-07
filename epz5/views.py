from django.shortcuts import render
from . models import faq_Page
from django.db.models import Q
from epz7.forms import EmailSignupForm
# Create your views here.

def list_faqs(request):
    pages = faq_Page.objects.order_by('-created')
    if request.user.is_staff or request.user.is_superuser:
        pages = faq_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = faq_Page.objects.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(created__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    return render(request, 'faq_page.html', {'pages': pages, 'forms': forms})
