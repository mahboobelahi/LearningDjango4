from django.shortcuts import render, redirect
from . import models
from .forms import ReviewForm
from django.urls import reverse
# Create your views here.

def rental_review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print(f'[X] {form.cleaned_data}')
            return redirect( reverse( 'cars_feedback:thank_you'))
    else:
        form = ReviewForm()
    
    return render(request, 'cars_feedback/rental_review.html',
                        context={'form': form})


def thank_you(request):

    return render(request, 'cars_feedback/thank_you.html')
