from django.shortcuts import render
from django.views.generic import (TemplateView,FormView,CreateView,ListView)
from .forms import ContactForm
from django.urls import reverse,reverse_lazy
from .models import Teacher
# Create your views here.

# def home_view(request):

#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    #! looks for template <model-name_form.html>
    fields = '__all__'
    #* success URL 
    #!please not it is a url not template
    success_url =reverse_lazy('classroom:greeting')# "/classroom/greeting/"

class TeacherListView(ListView):
    model = Teacher
    #! looks for template <model-name_list.html>
    #*by default context var name is "object_list"
    context_object_name = "teacher_list" #! this is how we can overwrite default context var name.
    #? we can also add custom query by overwriting default queryset
    #queryset = Teacher.objects.all() #!default quetset
    queryset = Teacher.objects.order_by('first_name')    #* custom queryset


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #* success URL
    #!please not it is a url not template
    success_url =reverse_lazy('classroom:greeting')# "/classroom/greeting/"

    #? What to do with this form?
    #! check validity of form by using class method
    #* if form is valid following method automatically called by Django
    def form_valid(self,form):
        #TODO Do whatever you want to do with cleaned data
        print(f"[X] {form.cleaned_data}")

        return super().form_valid(form)