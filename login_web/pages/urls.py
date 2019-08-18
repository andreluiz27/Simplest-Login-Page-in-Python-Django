# pages/urls.py
from django.urls import path

from .views import HomePageView, signup

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
     path('signup/', signup, name='signup')
]