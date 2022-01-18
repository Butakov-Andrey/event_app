from django.urls import path
from .views import AccountList, ApplicationList, EventList
from .views import EventDetail, RespondList

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/<int:pk>', EventDetail.as_view()),
    path('account/', AccountList.as_view()),
    path('application/', ApplicationList.as_view()),
    path('respond/', RespondList.as_view()),
]
