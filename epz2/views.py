from django.shortcuts import render
# Create your views here.

def list_about(request):
    return render(request, 'about_page.html', {})
