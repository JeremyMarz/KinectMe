from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Profile


class Dash(generic.ListView):
    model = Profile
    template_name = 'site/event_description.html'
    context='Profile'