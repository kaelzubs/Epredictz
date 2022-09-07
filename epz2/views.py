from django.shortcuts import render
from . models import About_Page
from django.db.models import Q
from epz7.forms import EmailSignupForm
# Create your views here.

def list_about(request):
    pages = About_Page.objects.order_by('-created')
    if request.user.is_staff or request.user.is_superuser:
        pages = About_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = About_Page.objects.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(created__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    return render(request, 'about_page.html', {'pages': pages, 'forms': forms})
