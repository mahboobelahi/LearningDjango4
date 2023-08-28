from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projectIndex(request):

    return HttpResponse("<h1> Hello this is a view inside tutorial Project !<h1>")