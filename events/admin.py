from django.contrib import admin

from .models import Application, Event, Respond


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'created_at',
        'started_at',
        'author',
    )


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'event',
        'created_at',
    )


class RespondAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'event',
        'created_at',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Respond, RespondAdmin)
