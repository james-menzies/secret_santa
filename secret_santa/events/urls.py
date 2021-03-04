from django.contrib.auth.decorators import login_required
from django.urls import path

from events.views import create, give_gift, edit_event, EventListView, activate_event, event_view

urlpatterns = [
    path('new/', create, name="create_event"),
    path('', login_required(EventListView.as_view()), name="view_all_events"),
    path('<int:pk>/', event_view, name="view_event"),
    path('<int:pk>/give/', give_gift, name="give_gift" ),
    path('<int:pk>/edit/', edit_event, name="edit_event"),
    path('<int:pk>/activate/', activate_event, name="activate_event"),
]
