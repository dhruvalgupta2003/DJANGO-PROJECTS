from django.urls import path
from . import views 
#URL Conf
urlpatterns = [
    path('welcome/',views.welcome)
]