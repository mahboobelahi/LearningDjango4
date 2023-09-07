from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('greeting/', views.ThankYouView.as_view(), name='greeting'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', views.TeacherListView.as_view(), name='list_teacher'),

]
