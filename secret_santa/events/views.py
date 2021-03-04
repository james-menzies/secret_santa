import random
from datetime import datetime, timedelta

from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView

from events.forms import EventForm, EmailFormSet
from events.models import Event, Gift
from users.models import CustomUser


def create(request):
    if request.method == 'POST':
        event_form = EventForm(data=request.POST, files=request.FILES)
        email_formset = EmailFormSet(request.POST, prefix='emails')

        if event_form.is_valid() and email_formset.is_valid():
            event = event_form.save(commit=False)
            event.owner = request.user
            event.save()

            emails = [form["email"] for form in email_formset.cleaned_data if
                      form and form["email"]]
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


class EventListView(ListView):
    model = Event
    allow_empty = True
    template_name = 'events/events.html'

    def get_queryset(self):
        return Event.objects.filter(participants__email=self.request.user.email)


class EventView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_view.html'

    def get_queryset(self):
        qs = super(EventView, self).get_queryset()
        return qs.filter(participants__email=self.request.user.email)


def give_gift(request, event_id: int):
    return render(request, 'events/edit_gift.html', context={"id": event_id})


def edit_event(request, event_id: int):
    return render(request, 'events/edit_event.html', context={"id": event_id})

def activate_event(request, pk: int):

    qs = Event.objects.filter(owner__email=request.user.email)
    event = get_object_or_404(qs, pk=pk)
    participants = list(event.participants.all())

    if len(participants) < 3 or event.status != Event.EventStatus.INACTIVE:
        return HttpResponseBadRequest()


    random.shuffle(participants)
    gifts = []

    for index, participant in enumerate(participants):

        gift = Gift()
        gift.donor = participant
        gift.recipient = participants[index - 1]
        gift.event_id = pk
        gifts.append(gift)

    Gift.objects.bulk_create(gifts)
    event.status = Event.EventStatus.ACTIVE
    conclusion = datetime.now() + timedelta(minutes=event.game_length)
    event.conclusion = conclusion

    # todo create async task that concludes event

    event.save()
    return redirect('view_event', pk=pk)



