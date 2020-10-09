from django.urls import path
from . import views

#from KinectMe.WebApp.views import dashboard

app_name = 'home'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.Add, name='signup'),
    path('update/', views.Update, name='update'),
    path('events/', views.events, name='events'),

]