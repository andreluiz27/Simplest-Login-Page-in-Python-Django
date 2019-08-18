from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView, signup


urlpatterns = [
    path('admin/', admin.site.urls),
  #z  path('', include('allauth.urls')),
    path('', include('pages.urls')),
    path('signup/', signup, name='signup'),
    path('', include('allauth.urls'), name='login')

]
