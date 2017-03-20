from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def jobs(request):
    return render(request, 'jobs.html', {})


def team(request):
    return render(request, 'team.html', {})
