from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    # return HttpResponse("Hello, welcome to Home Page")
    return render(request, 'index.html')

