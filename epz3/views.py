from django.shortcuts import render, redirect
from . forms import ContactForms
from django.core.mail import send_mail, get_connection
from epz7.forms import EmailSignupForm
# Create your views here.

def list_contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForms(request.POST or None)
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

    return render(request, 'contact_page.html', {
        'form': form,
        'submitted': submitted,
        'forms': forms
    })


def contact_success(request):
    forms = EmailSignupForm()
    return render(request, 'contact_success.html', {'forms': forms})



