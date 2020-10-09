from django.urls import path
from . import views

#from KinectMe.WebApp.views import dashboard

app_name = 'webapp'
urlpatterns = [
    path('', views.Dash.as_view(), name='Dash'),
    #path('admin/', admin.site.urls),
    #path('site/', dashboard)
]