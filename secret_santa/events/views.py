from django.forms import formset_factory
from django.shortcuts import render, redirect

# Create your views here.
from events.forms import EventForm, EmailForm, EmailFormSet
from users.models import CustomUser


def create(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
        email_formset = EmailFormSet(request.POST, prefix='emails')

        if event_form.is_valid() and email_formset.is_valid():
            event = event_form.save(commit=False)
            event.owner = request.user
            event.save()

            emails = [form["email"] for form in email_formset.cleaned_data if form and form["email"]]
            participants = CustomUser.objects.all().filter(email__in=emails)
            for participant in participants:
                event.participants.add(participant)

            event.participants.add(event.owner)
            event.save()

            return redirect('view_event', event_id=event.id)
        else:
            return redirect('create_event')
    else:
        event_form = EventForm()
        formset = EmailFormSet(prefix='emails')
        context = {
            "event_form": event_form,
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
