from rest_framework import generics, permissions

from .models import Application, Event, Respond
from .serializers import AccountSerializer, ApplicationSerializer
from .serializers import EventSerializer, RespondSerializer


class EventList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class RespondList(generics.ListCreateAPIView):
    queryset = Respond.objects.all()
    serializer_class = RespondSerializer


class AccountList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = AccountSerializer
