from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

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

    def create(self, request, *args, **kwargs):
        response = super(ApplicationList, self).create(request, *args, **kwargs)
        event = Event.objects.get(id=self.request.POST["event"])
        send_mail(
            subject=f'Application on event {self.request.POST["event"]}',
            message=f'''
            You have an application on event from user: {self.request.user}
            Application text: {self.request.POST["text"]}
            ''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[get_user_model().objects.get(username=event.author).email],
        )
        return response


class RespondList(generics.ListCreateAPIView):
    queryset = Respond.objects.all()
    serializer_class = RespondSerializer

    def create(self, request, *args, **kwargs):
        response = super(RespondList, self).create(request, *args, **kwargs)
        event = Event.objects.get(id=self.request.POST["event"])
        send_mail(
            subject=f'Respond on event {self.request.POST["event"]}',
            message=f'''
            You have an respond on event from user: {self.request.user}
            Respond text: {self.request.POST["text"]}
            ''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[get_user_model().objects.get(username=event.author).email],
        )
        return response


class AccountList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AccountSerializer

    def get_queryset(self):
        author = self.request.user
        return Event.objects.filter(author=author)
