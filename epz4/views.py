from django.shortcuts import render

# Create your views here.

def list_disclaim(request):
    return render(request, 'disclaimer_page.html', {})
