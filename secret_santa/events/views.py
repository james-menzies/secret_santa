import random
from datetime import datetime, timedelta
from typing import List

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic import ListView

from events.forms import EventForm, EmailFormSet, GiftForm, EmailFormSetHelper
from events.models import Event, Gift
from users.models import CustomUser

@login_required
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
            context = {
                'email_formset': email_formset,
                'email_formset_helper': EmailFormSetHelper(),
                'event_form': event_form,
                'title': "New Event"
            }
            return render(request, 'events/edit_event.html', context=context)
    else:
        event_form = EventForm()
        formset = EmailFormSet(prefix='emails')
        context = {
            "title": "New Event",
            "event_form": event_form,
            "email_formset": formset,
            "email_formset_helper": EmailFormSetHelper()
        }
        return render(request, 'events/edit_event.html', context=context)

@login_required
def edit_event(request, pk: int):
    qs = Event.objects.filter(owner__email=request.user.email).prefetch_related('participants')
    event: Event = get_object_or_404(qs, pk=pk)
    context = {
        "title": f"Editing {event.name}",
        "email_formset_helper": EmailFormSetHelper()
    }

    if request.method == 'POST':
        email_formset = EmailFormSet(data=request.POST, prefix='emails')
        event_form = EventForm(instance=event, data=request.POST)

        if email_formset.is_valid() and event_form.is_valid():
            updated_emails = [form["email"] for form in email_formset.cleaned_data if
                              form and form["email"]]
            updated_participants = CustomUser.objects.all().filter(email__in=updated_emails)
            current_participants = event.participants.all()

            for participant in current_participants:
                if participant not in updated_participants:
                    event.participants.remove(participant)

            for participant in updated_participants:
                if participant not in current_participants:
                    event.participants.add(participant)

            event.save()

            return redirect('view_event', pk=pk)
        else:
            context["email_formset"] = email_formset
            context["event_form"] = event_form
            return render(request, 'events/edit_event.html', context=context)


    else:
        if event.status == Event.EventStatus.INACTIVE:

            event_form = EventForm(instance=event)
            emails = [user.email for user in event.participants.all()]
            initial = [{"email": email} for email in emails]
            email_form = EmailFormSet(initial=initial, prefix='emails')
            context["event_form"] = event_form
            context["email_formset"] = email_form
            return render(request, 'events/edit_event.html', context=context)

        else:
            return redirect('view_event', pk=pk)


class EventListView(ListView):
    model = Event
    allow_empty = True
    template_name = 'events/events.html'
    extra_context = {
        "title": "My Events"
    }

    def get_queryset(self):
        qs = Event.objects.filter(participants__email=self.request.user.email)
        qs = qs.filter(Q(owner__email=self.request.user.email) | Q(concluded_at__isnull=False))
        qs = qs.order_by('-concluded_at')
        return qs

@login_required
def event_view(request, pk: int):
    qs = Event.objects.filter(id=pk).filter(participants__email=request.user.email)

    try:
        event = qs.get()
    except ObjectDoesNotExist:
        return redirect('landing_page')

    context = {"event": event,
               "title": event.name}
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
                if not gift.opened and gift.recipient == request.user:
                    return gift

        gifts = event.gifts \
            .prefetch_related('donor') \
            .prefetch_related('recipient').all()

        user_gift = get_user_gift(gifts)
        if user_gift:
            context["user_gift"] = user_gift
            user_gift.opened = True
            user_gift.save()
            return render(request, 'events/event_view_opening.html', context=context)
        else:
            context["gifts"] = gifts
            return render(request, 'events/event_view_reveal.html', context=context)

@login_required
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

@login_required
def activate_event(request, pk: int):
    qs = Event.objects.filter(owner__email=request.user.email)
    event: Event = get_object_or_404(qs, pk=pk)
    participants = list(event.participants.all())

    if len(participants) < 3 or event.status != Event.EventStatus.INACTIVE:
        messages.error(request, "You must have three participants as a minimum to activate event")
        return redirect('view_event', pk=pk)

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
