from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Profile, Event
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from WebApp.forms import *
from django.urls import reverse
from django.contrib.auth import logout


def homepage(request):
    context ={
        'Profile':Profile,
    }
    return render(request, 'site/homepage.html', context=context)

def signup(request):
    return render(request, 'site/signup.html')

def login(request):
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)


#@logout_required(login_url='/accounts/login/')
def Add(request):

    logout_view(request)

    form = AddForm(request.POST)
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            User.objects.create(username=user_name)
            user = User.objects.get(username=user_name)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            Profile.objects.create(user_name=user_name)
            profile = Profile.objects.get(user_name=user.username)
            profile.user = user
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.email = form.cleaned_data['email']
            profile.age = form.cleaned_data['age']

            profile.save()
            
        return HttpResponseRedirect(reverse( 'home:homepage') )
    else:
        form = AddForm(request.POST)
        context = {
            'form': form,
        }
    return render(request, "site/signup.html", context)

class Dash(generic.ListView):
    model = Profile
    template_name = 'site/event_description.html'
    context='Profile'
