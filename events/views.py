from rest_framework import generics

from .models import Application, Event
from .serializers import EventDetSerializer, EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


"""class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer"""


class ApplicationList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetSerializer
