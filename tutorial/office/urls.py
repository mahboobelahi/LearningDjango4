from django.urls import path
from . import views

#* domain.com/office ---> list all patient
urlpatterns = [
    path('', views.list_patients, name='list_patients')
]