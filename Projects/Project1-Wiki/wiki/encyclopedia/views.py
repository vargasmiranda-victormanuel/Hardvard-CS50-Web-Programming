from django.shortcuts import render
from markdown import Markdown
import secrets

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def specific_title(request, title):
    #if title is None:
    #    possible_pages = util.list_entries()
    #    title = possible_pages[0]

    page_content = md_to_html(title)
    if page_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "The wiki page " + title + " does not exists."
        })
    else:
        return render(request, "encyclopedia/specific_title.html", {
            "title": title,
            "page_content": page_content
        })

def md_to_html(title):
    #gets markdown format and convert it to html
    page_content = util.get_entry(title)
    markdown = Markdown()
    if page_content is None:
        return None
    else:
        return markdown.convert(page_content)

def search(request):
    #searches for a title in the encyclopedia
    if request.method == 'POST':
        search_query = request.POST['q']
        page_content = md_to_html(search_query)
        if page_content is not None:
            return render(request, "encyclopedia/specific_title.html", {
                "title": search_query,
                "page_content": page_content
            })
        else:
            wiki_pages = util.list_entries()
            match_pages = []
            for wiki_page in wiki_pages:
                if search_query.lower() in  wiki_page.lower():
                    match_pages.append(wiki_page)
            return render(request, "encyclopedia/search.html", {
                "match_pages": match_pages
            })
        
def new_wiki_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_wiki_page.html")
    elif request.method == 'POST':
        title = request.POST['title']
        previous_page_content = util.get_entry(title)
        if previous_page_content is not None:
            return render(request, "encyclopedia/error.html", {
                "error_message": "the wiki page " + title + " already exists."
            })
        else:
            md_content = request.POST['md_content']
            md_content = md_content.replace("\r", "")
            util.save_entry(title, md_content)
            return render(request, "encyclopedia/specific_title.html", {
                "title": title,
                "page_content": md_to_html(title)
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['entry']
        md_content = util.get_entry(title)
        md_content = md_content.replace("\r", "")
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "md_content": md_content
        })
    
def save_page(request):
    if request.method == "POST":
        title = request.POST['title']
        md_content = request.POST['md_content']
        util.save_entry(title, md_content)
        return render(request, "encyclopedia/specific_title.html", {
            "title": title,
            "page_content": md_to_html(title)
        })
    
def random_page(request):
    wiki_pages = util.list_entries()
    random_page_selected = secrets.choice(wiki_pages)

    page_content = md_to_html(random_page_selected)

    return render(request, "encyclopedia/specific_title.html", {
        "title": random_page_selected,
        "page_content": page_content
    })