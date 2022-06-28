from django.shortcuts import render

from . import util
import markdown #using pip install
import random #random module


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_to_HTML(title):
    entry=util.get_entry(title)
    html=markdown.markdown(entry) if entry else None

    return html


    def entry(request,title):
        entryPage=util.get_entry(title)
