from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    f = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        'flight': f,
        "passengers":f.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=f).all()
    })

def book(request, flight_id):
    if request.method == 'POST':
        f = Flight.objects.get(pk=flight_id)
        p = Passenger.objects.get(pk=int(request.POST["passenger"]))
        p.flights.add(f)
        return HttpResponseRedirect(reverse("flight", args=(f.id,)))
