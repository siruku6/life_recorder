from django.shortcuts import render


def index(request):
    return render(request, 'cms/index.html.haml')
