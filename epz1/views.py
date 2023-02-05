from django.shortcuts import render
from . models import Home_Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from epz7.forms import EmailSignupForm
from datetime import datetime, timedelta
from itertools import groupby
from operator import attrgetter
from django.db.models.functions import TruncDate


def list_home_prev(request):
    queryset = Home_Page.objects.annotate(
        created_at_date=TruncDate('date_time'),
    ).order_by('date_time')
    pages = groupby(queryset, attrgetter('created_at_date'))
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)

        ).distinct()

    paginator = Paginator(pages, 5)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page()
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })

def list_home_today(request):
    queryset = Home_Page.objects.annotate(
        created_at_date=TruncDate('date_time'),
    ).order_by('date_time')
    pages = groupby(queryset, attrgetter('created_at_date'))
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)

        ).distinct()

    paginator = Paginator(pages, 5)
    page = request.GET.get('page')
    try:
        ppages = paginator.page(page)
    except PageNotAnInteger:
       ppages = paginator.page()
    except EmptyPage:
        ppages = paginator.page(paginator.num_pages)

    forms = EmailSignupForm()

    return render(request, 'home_page.html', {
        'pages': pages,
        'ppages': ppages,
        'forms': forms
    })


def list_home(request):
    queryset = Home_Page.objects.annotate(
        created_at_date=TruncDate('date_time'),
    ).order_by('date_time')
    pages = groupby(queryset, attrgetter('created_at_date'))
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)

        ).distinct()

    paginator = Paginator(pages, 5)
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

def list_home_next(request):
    queryset = Home_Page.objects.annotate(
        created_at_date=TruncDate('date_time'),
    ).order_by('date_time')
    pages = groupby(queryset, attrgetter('created_at_date'))
    query = request.GET.get('q')
    if query:
        pages = Home_Page.objects.filter(
            Q(date_time__icontains=query) |
            Q(league__icontains=query) |
            Q(home_team__icontains=query) |
            Q(away_team__icontains=query) |
            Q(tip__icontains=query) |
            Q(tip_odd__icontains=query) |
            Q(result__icontains=query)

        ).distinct()

    paginator = Paginator(pages, 5)
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
    response = render(request, "error_404.html", {})
    response.status_code = 404
    return response


def handler500(request, template_name="error_500.html"):
    pages = Home_Page.objects.all()
    response = render(request, "error_500.html", {})
    response.status_code = 500
    return response

