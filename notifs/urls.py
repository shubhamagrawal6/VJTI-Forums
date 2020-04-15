from django.contrib import admin
from django.urls import path
from .views import (
    NotifListView,
    NotifDetailView,
)
from blog import views
urlpatterns = [
    path('', NotifListView.as_view(), name='notifs-home'),
    path('<int:pk>', NotifDetailView.as_view(), name='notifs-detail'),
]