from django import forms
from django.forms import ModelForm
from .models import Review


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here.',
#                              widget=forms.Textarea())

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            'first_name':"YOUR FIRST NAME",
            'last_name':"Last Name",
            'stars':'Rating'
        }
        error_messages = {
            'stars':{
                'min_value':'YO! Min value is 1.',
                'max_value':'YO! YO! Max value is 5.'
            }
        }
