from django.shortcuts import render , redirect
from django.contrib import messages
# Create your views here.

from .forms import *
from .models import *



def addevent(request):
    
    if request.method=="POST":
        if request.user.is_authenticated:
            form=EventForm(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                event=Event.objects.get(name=request.POST["name"])
                messages.success(request, "You have posted your event")             
                event.manager = request.user
                event.save()
                return redirect('home')
            else:
                messages.success("Please enter valid Information")
                return redirect('addevent')
        else:
            messages.success(request , "Please login first.")                        
            return redirect('login')
    else:
        form=EventForm()
        return render(request, "events/addevent.html",{
                "form":form     
        })
    
def all_events(request):
    events=Event.objects.all()
    return render(request, "events/events.html",{
        "events":events
    })

def show_event(request, event_id):
    event=Event.objects.get(pk=event_id)
    return render(request, "events/event.html",{
        "event":event
    })

def addvenue(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            form=VenueForm(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                messages.success(request, "You have Added the Venue")            
                return redirect('home')
            else:
                messages.success("Please enter valid Information")
                return redirect('addvenue')
        else:
            messages.success(request , "Please login first.")                        
            return redirect('login')
    else:
        form=EventForm()
        return render(request, "events/addvenue.html",{
                "form":form     
        })