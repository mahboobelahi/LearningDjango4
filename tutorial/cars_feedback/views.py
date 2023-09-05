from django.shortcuts import render
from . import models
# Create your views here.

def rental_review(request):


     
    return render(request,'cars_feedback/rental_review.html')

def thank_you(request):


     
    return render(request,'cars_feedback/thank_you.html')