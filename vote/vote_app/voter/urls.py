from django.urls import path
from .views import voter_application

urlpatterns = [
    path('', voter_application, name='voter_application'),
]
