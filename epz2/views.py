from django.shortcuts import render
from epz7.forms import EmailSignupForm
# Create your views here.

def list_about(request):
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
    return render(request, 'about_page.html', {
        'pages': pages,
        'forms': forms
    })
