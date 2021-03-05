import random
from datetime import datetime, timedelta
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic import ListView

from events.forms import EventForm, EmailFormSet, GiftForm
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

            return redirect('view_event', pk=event.id)
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


def event_view(request, pk: int):
    qs = Event.objects.filter(id=pk).filter(participants__email=request.user.email)

    try:
        event = qs.get()
    except ObjectDoesNotExist:
        return redirect('landing_page')

    context = {"event": event}
    # this is to prevent multiple datetime.now() calls
    status = event.status

    if status == Event.EventStatus.INACTIVE:
        participants = event.participants.all()
        context["participants"] = participants
        return render(request, 'events/event_view_inactive.html', context=context)

    elif status == Event.EventStatus.ACTIVE:

        gift = event.gifts.filter(donor__email=request.user.email).get()
        context["gift"] = gift
        return render(request, 'events/event_view_active.html', context=context)
    else:

        def get_user_gift(gifts: List[Gift]) -> Gift:
            for gift in gifts:
                if gift.opened and gift.recipient == request.user:
                    return gift

        gifts = event.gifts.all()
        user_gift = get_user_gift(gifts)
        context["user_gift"] = user_gift
        if user_gift:
            return render(request, 'events/event_view_opening.html', context=context)

    return render(request, 'events/event_view.html', {"event": event})


def give_gift(request, pk: int):
    qs = Gift.objects \
        .filter(event_id=pk) \
        .filter(donor__email=request.user.email) \
        .filter(emoji_id__isnull=True)

    try:
        gift = qs.get()
        if gift.event.status != Event.EventStatus.ACTIVE:
            raise ValueError()
    except (ObjectDoesNotExist, ValueError):
        return redirect('view_event', pk=pk)

    if request.method == 'POST':
        form = GiftForm(data=request.POST, instance=gift)
        if form.is_valid():
            form.save()
            return redirect('view_event', pk=pk)
    else:

        form = GiftForm(instance=gift)
        return render(request, 'events/edit_gift.html', context={
            'form': form,
            'gift': gift,
        })


def edit_event(request, event_id: int):
    return render(request, 'events/edit_event.html', context={"id": event_id})


def activate_event(request, pk: int):
    qs = Event.objects.filter(owner__email=request.user.email)
    event: Event = get_object_or_404(qs, pk=pk)
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
    event.activated_at = datetime.now()
    conclusion = event.activated_at + timedelta(minutes=event.game_length)
    event.concluded_at = conclusion

    event.save()
    return redirect('view_event', pk=pk)
