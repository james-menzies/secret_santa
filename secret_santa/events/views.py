from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create(request):

    return HttpResponse("The create event page")

def view_all(request):
    return HttpResponse("The view all events page")

def view_single(request, event_id: int):

    return HttpResponse("The view single event page")

def give_gift(request, event_id: int):

    return HttpResponse("The give a gift page")
