from django.shortcuts import render
from . models import Home_Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from epz7.forms import EmailSignupForm
from django.contrib.sitemaps import Sitemap
import os
from ratelimit import limits
import requests



# @limits(calls=10, period=1)
# def rate_limiter():
#     url = os.getenv('DAILY_URL')
#     querystring = {"sort":"-id"}
#     headers = {
#         "Content-Type": "application/json",
#         "Connection": "keep-alive",
#         "X-RapidAPI-Key": os.getenv('DAILY_RAPIDAPI_KEY'),
#         "X-RapidAPI-Host": os.getenv('DAILY_RAPIDAPI_HOST')
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     data = response.json()
#     arrdata = data['data']
#     for dt in arrdata:
#         for res in dt['coupons_list_data']:
#             if not Home_Page.objects.filter(
#                 match_dat = res['match_date'],
#                 match_time = res['match_time'],
#                 league = res['league_name'],
#                 home_team = res['home_team'],
#                 away_team = res['away_team'],
#                 tip = res['game_prediction'],
#                 tip_odd = res['odd_value'],
#                 result = res['match_status']
#                 ).exists():
#                 Home_Page.objects.create(
#                     match_dat = res['match_date'],
#                     match_time = res['match_time'],
#                     league = res['league_name'],
#                     home_team = res['home_team'],
#                     away_team = res['away_team'],
#                     tip = res['game_prediction'],
#                     tip_odd = res['odd_value'],
#                     result = res['match_status']
#                 )
    
# rate_limiter()

def list_home(request):
    pages = Home_Page.objects.all().order_by('-match_dat')
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all().order_by('-match_dat')

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)

        ).distinct()

    paginator = Paginator(pages, 10)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page(1)
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })


def handler404(request, exception, template_name="error_404.html"):
    pages = Home_Page.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    response = render(request, "error_404.html", {
        'pages': pages,
        'forms': forms
    })
    response.status_code = 404
    return response


def handler500(request, template_name="error_500.html"):
    pages = Home_Page.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        pages = Home_Page.objects.all()

    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(match_dat__icontains=query) |
            Q(country__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)
        ).distinct()

    forms = EmailSignupForm()

    response = render(request, "error_500.html", {
        'pages': pages,
        'forms': forms
    })
    response.status_code = 500
    return response

