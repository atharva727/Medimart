from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static  

from prescription.views import *

urlpatterns = [    
    path('', Index.as_view(),name='home'),
    path('login/', Login.as_view(),name='login'),    
    path('logout/', Login.logout, name="logout"),
    path('signup/', Signup.as_view(),name='signup'),
    path('prescription/', Prescription.as_view(),name='prescription'),
    path('result/', Result.as_view(), name='result'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
