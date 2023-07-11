from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def pages(request, page):
    return render(request, "encyclopedia/pages.html", {
        'page': page
    })