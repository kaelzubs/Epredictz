from django.shortcuts import render

# Create your views here.
def invest_view(request):
    return render(request, 'invest.html', {})
