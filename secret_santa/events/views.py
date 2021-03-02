from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create(request):

    return render(request, 'events/edit_event.html')

def view_all(request):
    return render(request, 'events/events.html')

def view_single(request, event_id: int):
    return render(request, 'events/event_view.html', context={"id": event_id})

def give_gift(request, event_id: int):
    return render(request, 'events/edit_gift.html', context={"id": event_id})

def edit_event(request, event_id: int):
    return render(request, 'events/edit_event.html', context={"id": event_id})
