from django.forms import formset_factory
from django.shortcuts import render, redirect

# Create your views here.
from events.forms import EventForm, EmailForm, EmailFormSet


def create(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('view_event', event_id=event.id)
        else:
            return redirect('create_event')
    else:
        form = EventForm()
        formset = EmailFormSet(prefix='emails')
        context = {
            "event_form": form,
            "email_formset": formset
        }
        return render(request, 'events/edit_event.html', context=context)

def view_all(request):
    return render(request, 'events/events.html')

def view_single(request, event_id: int):
    return render(request, 'events/event_view.html', context={"id": event_id})

def give_gift(request, event_id: int):
    return render(request, 'events/edit_gift.html', context={"id": event_id})

def edit_event(request, event_id: int):
    return render(request, 'events/edit_event.html', context={"id": event_id})
