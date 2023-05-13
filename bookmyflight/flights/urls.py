from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns=[
    path("",views.land,name="land"),
    path("save_message",views.save_message,name="save_message"),

    
    
 
 ]

urlpatterns += staticfiles_urlpatterns()