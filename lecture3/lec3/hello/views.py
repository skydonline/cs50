from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello-folder/index.html")

def sky(request):
    return HttpResponse("Hello, Sky!")

def joe(request):
    return HttpResponse("Joe Schmoe")

def greet(request, name):
    return render(request, "hello-folder/greet.html", {
        'name': name.capitalize()
    })