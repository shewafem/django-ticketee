from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview),
    path('event-list/', eventList),
    path('event-detail/<int:pk>/', eventDetail),
    path('event-create/', eventCreate),
    path('event-update/<int:pk>/', eventUpdate),
]