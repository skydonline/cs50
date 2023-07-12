from django.shortcuts import render
import markdown
import os
from django.shortcuts import redirect
from . import util
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, pagename):
    entry = util.get_entry(pagename)
    if entry is None:
        return render(request, 'encyclopedia/404.html', {
            'pagename':pagename
        })
    html_content = markdown.markdown(entry)
    return render(request, 'encyclopedia/wikipedia.html', {
        'html_content': html_content, 
        'pagename':pagename
        })

def search(request):
    query = request.GET.get('q')
    page_exists = util.get_entry(query)
    if page_exists is None:
        results = util.search_entry(query)
        return render(request, 'encyclopedia/search.html', {
            'results': results,
            'query': query
        })
    html_content = markdown.markdown(page_exists)
    return render(request, 'encyclopedia/wikipedia.html', {
        'html_content': html_content,
        'pagename': query
    })