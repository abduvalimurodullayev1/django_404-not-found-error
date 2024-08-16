from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


def index(request):
    return HttpResponse("Hello, world. You're at the Home page of Django sample project error 404.")
