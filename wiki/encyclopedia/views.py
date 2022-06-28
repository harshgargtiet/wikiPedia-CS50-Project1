from this import s
from django.shortcuts import render
from . import util
import markdown 
#using pip install
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
        if entryPage is None: 
            return render(request,"encyclopedia/nonExistingEntry.html",{
                "entryTitle": title
            }) 
        else: 
                  return render(request,"encyclopedia/entry.html",{
                    "entry": convert_to_HTML(title),
                    "entryTitle":title
                })

def search(request):
    if request.method=='GET':
        input=request.GET.get('q')
        html = convert_to_HTML(input)
        entries=util.list_entries()
        search_pages=[]

    for entry in entries:
            if input.upper in entry.upper():
                search_pages.append(entry)

    for entry in entries:
            if input.upper()==entry.upper():
                return render(request,"encyclopedia/entry.html",{
                    "entry":html,
                    "entryTitle":input
                })

    else:
        return render(request,"encyclopedia/nonExistingEntry.html",{
            "entryTitle":input
        })


def newPage(request):
    return render(request,"encylopedia/newPage.html")

def save(request):
    if request.methos =='POST':
        input_title=request.POST['title']
        input_text=request.POST['text']
        entries=util.list_entries()

        html=convert_to_HTML(input_title)

        Already_exist_true="false"
        for entry in entries:
            if input_title.upper()==entry.upper():
                Already_exist_true="true"

        if Already_exist_true=="true":
            return render(request,"encylopedia/already_exist.html",{
                "entry":html,
                "entryTitle":input_title
            })
        else:
          util.save_entry(input_title, input_text)
          return render(request, "encyclopedia/entry.html", {
				"entry": convert_to_HTML(input_title),
				"entryTitle": input_title
			})


def randomPage(request):
	
	entries = util.list_entries()

	randEntry = random.choice(entries)

	html = convert_to_HTML(randEntry)
	
	return render(request, "encyclopedia/entry.html",{
		"entry": html,
		"entryTitle":randEntry
		})

def editPage(request): 

	if request.method == 'POST':
	
		input_title = request.POST['title']
		
		text = util.get_entry(input_title)
		
		
		return render(request, "encyclopedia/editPage.html",{
			"entry": text,
			"entryTitle": input_title
		})

def saveEdit(request):
	
	if request.method == 'POST':
		
		entryTitle = request.POST['title']
		entry = request.POST['text']
		
		util.save_entry(entryTitle, entry)
		
		html = convert_to_HTML(entryTitle)
		return render (request, "encyclopedia/entry.html",{
			"entry": html,
			"entryTitle": entryTitle
			})