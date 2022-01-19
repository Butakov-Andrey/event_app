from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import filters, generics, permissions

from .models import Application, Event, Respond
from .serializers import (AccountSerializer, ApplicationSerializer,
                          EventSerializer, RespondSerializer)


class EventList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['type']


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def create(self, request, *args, **kwargs):
        response = super(ApplicationList, self).create(
            request, *args, **kwargs
            )
        event = Event.objects.get(id=self.request.POST["event"])
        author_email = [get_user_model().objects.get(
            username=event.author
            ).email]
        send_mail(
            subject=f'Application on event {self.request.POST["event"]}',
            message=f'''
            You have an application on event from user: {self.request.user}
            Application text: {self.request.POST["text"]}
            ''',
            from_email=settings.EMAIL_HOST_USER,
            # select event author's email
            recipient_list=author_email,
        )
        print([get_user_model().objects.get(
                username=event.author
                ).email])
        return response


class RespondList(generics.ListCreateAPIView):
    queryset = Respond.objects.all()
    serializer_class = RespondSerializer

    def create(self, request, *args, **kwargs):
        response = super(RespondList, self).create(
            request, *args, **kwargs
            )
        event = Event.objects.get(id=self.request.POST["event"])
        author_email = [get_user_model().objects.get(
            username=event.author
            ).email]
        send_mail(
            subject=f'Respond on event {self.request.POST["event"]}',
            message=f'''
            You have an respond on event from user: {self.request.user}
            Respond text: {self.request.POST["text"]}
            ''',
            from_email=settings.EMAIL_HOST_USER,
            # select event author's email
            recipient_list=author_email,
        )
        return response


class AccountList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AccountSerializer

    def get_queryset(self):
        # show event list with applications and responds of authorized user
        author = self.request.user
        return Event.objects.filter(author=author)
