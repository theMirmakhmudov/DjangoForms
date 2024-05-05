from django import forms
from apps.models import Contact


class InputContact(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    country = forms.CharField(label="Your Country", max_length=255)
    subject = forms.CharField(label="Subject", max_length=500)
