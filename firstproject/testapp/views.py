from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s='<h1> welcome to my first django view </h1>'
    return HttpResponse(s)
