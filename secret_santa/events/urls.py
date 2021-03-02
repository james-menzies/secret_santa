from django.urls import path

from events.views import create, view_all, view_single, give_gift, edit_event

urlpatterns = [
    path('new/', create, name="create_event"),
    path('', view_all, name="view_all_events"),
    path('<int:event_id>/', view_single, name="view_event"),
    path('<int:event_id>/give/', give_gift, name="give_gift" ),
    path('<int:event_id>/edit/', edit_event, name="edit_event")
]
