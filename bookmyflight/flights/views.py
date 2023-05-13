from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import os
from .models import Message
from django.urls import reverse

# Create your views here.
def land(request):
    return render(request,"flights/landing.html") 

def save_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
   
        message = Message(name = name,email = email,message = message)
        message.save()
        return redirect(reverse('land'))
    return redirect(reverse('land'))








