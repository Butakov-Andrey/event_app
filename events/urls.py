from django.urls import path
from .views import ApplicationList, EventList, EventDetail

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/<int:pk>', EventDetail.as_view()),
    path('account/', ApplicationList.as_view()),
]
