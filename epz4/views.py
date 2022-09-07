from django.shortcuts import render
from . models import Disclaim_Page
from django.db.models import Q
from epz7.forms import EmailSignupForm
# Create your views here.

def list_disclaim(request):
    pages = Disclaim_Page.objects.order_by('-created')
    if request.user.is_staff or request.user.is_superuser:
        pages = Disclaim_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Disclaim_Page.objects.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(created__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    return render(request, 'disclaimer_page.html', {'pages': pages, 'forms': forms})
