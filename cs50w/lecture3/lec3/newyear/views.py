from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    date = datetime.datetime.now()
    return render(request, "newyear-folder/index.html", {
        "newyear": date.month == 7 and date.day == 10
    })
