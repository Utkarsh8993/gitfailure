from django.urls import path

from . import views

urlpatterns = [
    path('addevent' , views.addevent , name = "addevent"),
    path('events' , views.all_events , name = "events" ),
    path('event/<int:event_id>' , views.show_event , name="event"),
    path('addvenue' , views.addvenue , name="addvenue"),
    path('venues' , views.all_venues , name="venues"),
    path('eventshome', views.home, name="eventshome"),
]