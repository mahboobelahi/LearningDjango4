from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound,
                         Http404, HttpResponseRedirect)
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello this is a view inside my_app !<h1>")


#! Dynamic urls save us from defining multiple views for several pages
# * can be done by using passing file or python obj (dict) containing page names
# articles = {
#     'sports': 'Sport Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }

# #* Mixing python obj into views
# def news_view(request, topic):
#     try:
#         # result = articles[topic]
#         print(f'[X-1] {topic},{articles.get(topic)} ')
#         return HttpResponse(f"<h1>{articles[topic]}<h1>")
#     except:
#          print(f'[X-11] {topic},{articles.get(topic)} ')
#          raise Http404("404 GENERIC ERROR")
#          #return HttpResponseNotFound(f"<h1>Page not found for topic: <em>{topic}</em></h1>")
#     # if articles.get(topic):
#     #     return HttpResponse(f"<h1>{articles[topic]}<h1>")
#     # else:
#     #     return HttpResponse(f"<h2>Page <em>'{topic}'</em> not found,</h2>.")

# #* redirecting pages
# def num_page_views(request,num_page):
#     try:
#         topics_list = list(articles.keys())
#         topic = topics_list[num_page]
#         # web_page = reverse('topic-page',args=[topic])
#         # print(f"[X-2] {topics_list}, {topic}, {web_page}")
#         return HttpResponseRedirect(reverse('topic-page',args=[topic]))
#     except:
#         raise Http404("404 GENERIC ERROR")

def simple_view(request):
    return render(request,'my_app/example.html') #*some html file from templete dir

def variable_view(request):
    my_var = {'first_name':'Mahboob', 'last_name':'Elahi',
              'some_list':[1,2,3], 'some_dictionary':{'inside_key':'inside_value'}}
    return render(request,'my_app/variable.html',context=my_var) #*some html file from templete dir






