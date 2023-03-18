from django.contrib import admin
from django.urls import path, include

from prescription.views import *

urlpatterns = [    
    path('', Index.as_view()),
    path('login/', Login.as_view()),
    path('prescription/', Prescription.as_view()),
    path('result/', Result.as_view()),
]
