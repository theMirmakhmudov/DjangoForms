from django.http import HttpResponse
from django.shortcuts import render
from apps.models import Contact
from apps.forms import InputContact


def forms(request):
    if (request.method == 'POST'):
        form = InputContact(request.POST)
        if (form.is_valid()):
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            subject = form.cleaned_data['subject']
            student = Contact.objects.create(first_name=first_name, last_name=last_name, country=country,
                                             subject=subject)
            student.save()
            return render(request, "created_success.html")

    contact_form = InputContact()
    return render(request, "index.html", {"form": contact_form})
