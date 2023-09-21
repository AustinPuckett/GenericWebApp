from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Person


def index(request):
    p = Person(first_name="Jody", last_name="Foster")
    p.save()
    response = ' '.join([p.first_name, p.last_name])
    return HttpResponse(response)