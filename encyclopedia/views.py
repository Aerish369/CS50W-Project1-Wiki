from django.shortcuts import render
from django.http import HttpResponse
import markdown
import random


from . import util

def md_to_html(title):
    """
    COmment
    """
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    """
    COMMENT
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    """
    Takes string as the endpoint and 
    Returns the detailed page about the title 
    """
    html_content = md_to_html(title)
    context = {"title": title, "content": html_content}
    if html_content == None:
        return render(request, "encyclopedia/error.html", context)
    else:
        return render(request, "encyclopedia/entry.html", context)

def search(request):
    if request.method == 'POST':
        entry_search = request.POST['q']
        html_content = md_to_html(entry_search)
        if html_content is not None:
            return render(request, 'encyclopedia/entry.html', {
                "title":entry_search,
                "content": html_content,
            })
        else:
            all_entries = util.list_entries()
            recommendation = []
            for entry in all_entries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            if recommendation == []:
                return render(request, "encyclopedia/error.html", {"title":entry_search})
            else:
                return render(request, "encyclopedia/recommend.html",{
                "recommendation": recommendation,
                })

def createPage(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        page = 'create-page'
        if title in util.list_entries():
            return render(request, 'encyclopedia/error.html', {'page':page, 'title':title})
        else:
            util.save_entry(title, content)
            htmlContent = md_to_html(title)
            return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'content': htmlContent,
            })
    return render(request, 'encyclopedia/create-page.html')


def editPage(request):
    if request.method == 'POST':
        title = request.POST['entryTitle']
        content = util.get_entry(title)
        return render (request, 'encyclopedia/edit-page.html',{
            'title':title,
            'content': content,
        })


def saveEdit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        htmlContent = md_to_html(title)
        return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'content': htmlContent,
            })
    

def randomPage(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    html_content = md_to_html(random_entry)
    return render(request, 'encyclopedia/entry.html', {
                'title': random_entry,
                'content': html_content,
            })
    

