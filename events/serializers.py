from xml.dom import ValidationErr

from rest_framework import serializers

from .models import Application, Event, Respond


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


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
        )

    class Meta:
        fields = (
            'id',
            'user',
            'event',
            'text',
            'created_at',
        )
        model = Application

    def validate(self, data):
        # validate event type (application for first type)
        event = Event.objects.get(name=data['event'])
        if event.type == '1':
            return data
        else:
            raise ValidationErr('Not your event')

    def save(self, **kwargs):
        # Add authorized user to field 'user'
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)


class RespondSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
        )

    class Meta:
        fields = (
            'id',
            'user',
            'event',
            'text',
            'created_at',
            'file',
        )
        model = Respond

    def validate(self, data):
        # validate event type (respond for second type)
        event = Event.objects.get(name=data['event'])
        if event.type == '2':
            return data
        else:
            raise ValidationErr('Not your event')

    def save(self, **kwargs):
        # Add authorized user to field 'user'
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'author',
            'name',
            'description',
            'type',
            'application_set',
            'respond_set',
        )
        model = Event
