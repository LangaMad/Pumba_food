from django.urls import path
from .views import *

urlpatterns = [
   path('contact_us/',ContactUsView.as_view(),name='contact_us')
]