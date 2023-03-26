from django.shortcuts import render
from .models import Menu


def Index(request):
    template = 'menu/index.html'
    context = {}
    return render(request, template, context)
