from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.
admin.site.register(Profile)
admin.site.register(Activities)
admin.site.register(Event)


