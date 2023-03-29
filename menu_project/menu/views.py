from django.shortcuts import render


def Index(request):
    template = 'menu/index.html'
    return render(request, template)
