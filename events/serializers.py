from rest_framework import serializers

from .models import Application, Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'author',
            'name',
            'description',
            'type',
            'created_at',
            'started_at',
        )
        model = Event


"""class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'user',
            'event',
            'text',
            'created_at',
        )
        model = Application"""


class EventDetSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'author',
            'name',
            'description',
            'type',
            'application_set',
        )
        model = Event
