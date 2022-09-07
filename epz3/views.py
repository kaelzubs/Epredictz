from django.shortcuts import render, redirect
from . models import Contact_Page
from . forms import ContactForms
from django.core.mail import send_mail, get_connection
from django.db.models import Q
from epz7.forms import EmailSignupForm
# Create your views here.

def list_contact(request):
    pages = Contact_Page.objects.order_by('-created')
    if request.user.is_staff or request.user.is_superuser:
        pages = Contact_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Contact_Page.objects.filter(
            Q(title__icontains=query) |
            Q(bodytext__icontains=query) |
            Q(created__icontains=query)
        ).distinct()

    submitted = False
    if request.method == 'POST':
        form = ContactForms(request.POST or None )
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@epredictz.com'),
                ['donmart4u@gmail.com'],
                connection=con
                )
            return redirect('contact_success')
    else:
            form = ContactForms()
            if 'submitted' in request.GET:
                submitted = True

    forms = EmailSignupForm()

    return render(request, 'contact_page.html', {'form': form, 'pages': pages, 'submitted': submitted, 'forms': forms})


def contact_success(request):
    forms = EmailSignupForm()
    return render(request, 'contact_success.html', {'forms': forms})



