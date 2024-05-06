from django import forms
from django.forms import ModelForm
from apps.models import Contact


# class InputContact(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=255)
#     last_name = forms.CharField(label="Last Name", max_length=255)
#     country = forms.CharField(label="Your Country", max_length=255)
#     subject = forms.CharField(label="Subject", max_length=500)

class InputContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
