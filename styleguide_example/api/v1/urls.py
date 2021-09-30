from django.urls import path
from django.urls import include

app_name = 'authentication'

urlpatterns = [
    path('authentication/',
         include('styleguide_example.authentication.v1.urls')),
    path('users/',
         include('styleguide_example.users.v1.urls')),
]
