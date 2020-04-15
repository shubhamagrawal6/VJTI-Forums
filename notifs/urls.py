from django.contrib import admin
from django.urls import path
from .views import (
    NotifListView,
    NotifDetailView,
    UserNotifListView,
)
from blog import views
urlpatterns = [
    path('', NotifListView.as_view(), name='notifs-home'),
    path('<int:pk>', NotifDetailView.as_view(), name='notifs-detail'),
    path('user/<str:username>/notifs', UserNotifListView.as_view(), name='user-notifs'),
]