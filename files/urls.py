from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.fileslist, name='fileslist'),
    path('upload/', views.upload, name='upload'),
]