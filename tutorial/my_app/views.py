from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello this is a view inside my_app !<h1>")


#! Dynamic urls save us from defining multiple views for several pages
# * can be done by using passing file or python obj (dict) containing page names
articles = {
    'sports': 'Sport Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request, topic):
    # try:
    #     return HttpResponse(f"<h1>{articles[topic]}<h1>")
    # except:
    #      print(f'[X] {articles[topic]} ')
    #      HttpResponse("<h1>Page was found</h1>")
    if articles.get(topic):
        return HttpResponse(f"<h1>{articles[topic]}<h1>")
    else:
        return HttpResponse(f"<h2>Page <em>'{topic}'</em> not found,</h2>.")
