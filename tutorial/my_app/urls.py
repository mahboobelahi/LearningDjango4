from django.urls import path
from . import views

#* registeres app namespace
#* and used for URL names
app_name = 'my_app'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:num_page>', views.num_page_views, name='num_news'),
    # path('<str:topic>/', views.news_view, name='topic-page'),
    path('', views.simple_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
]
