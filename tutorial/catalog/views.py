from django.shortcuts import render
from django.http import HttpResponse
from .models import (Genre,Author,Language,
                     Book,BookInstance)
from django.views.generic import (TemplateView,FormView,
                                  CreateView,ListView,
                                  DetailView,DeleteView,
                                  UpdateView)
# from .forms import ContactForm
from django.urls import reverse,reverse_lazy
# Create your views here.

def index_view(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()
    #! to make life easy always pass data to templates as a context dictinoary not just plain dict
    context = {"num_books":num_books,
               "num_instance":num_instance,
               "num_instance_available":num_instance_available
               }
    return render(request,'catalog/index.html',context={"context":context})



