from email.policy import default
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

    def save(self, **kwargs):
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

    def save(self, **kwargs):
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
