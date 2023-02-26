from django.shortcuts import render
from epz7.forms import EmailSignupForm
from epz1.models import Home_Page
# Create your views here.

def list_disclaim(request):
    pages = Home_Page.objects.filter(
        pub_date=datetime.now()
    )
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(pub_date__icontains=query) |
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
    
        ).distinct()

    forms = EmailSignupForm()

    return render(request, 'disclaimer_page.html', {
        'forms': forms,
        'pages': pages
    })
