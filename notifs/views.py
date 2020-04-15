from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Notif
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
)
from django.contrib.auth.decorators import login_required
def notifs(request):
    context={
        'notifs': Notif.objects.all()
    }
    return render(request, 'notifs/home.html',context)

class NotifListView(ListView):
    model= Notif
    template_name='notifs/home.html'
    context_object_name='notifs'
    ordering=['-date_posted']
    paginate_by=5

class NotifDetailView(DetailView):
    model= Notif
    template_name='notifs/notifs_detail.html'
    context_object_name='notifs'
