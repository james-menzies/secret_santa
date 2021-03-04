from django.contrib.auth.decorators import login_required
from django.urls import path

from events.views import create, give_gift, edit_event, EventListView, EventView

urlpatterns = [
    path('new/', create, name="create_event"),
    path('', login_required(EventListView.as_view()), name="view_all_events"),
    path('<int:pk>/', login_required(EventView.as_view()), name="view_event"),
    path('<int:event_id>/give/', give_gift, name="give_gift" ),
    path('<int:event_id>/edit/', edit_event, name="edit_event")
]
