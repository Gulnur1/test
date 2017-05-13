from django.shortcuts import render
from django.utils import timezone
from datetime import date

class Post:
    def __init__(self, id, title, text, author, date):
        self.id = id
        self.title = title
        self.text = text
        self.author = author
        self.date = date

class Author:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

authors = [
    Author(1, "dark_angel", "angel@hell.com"),
    Author(2, "elvis", "elvis@heaven.com"),
    Author(3, "dummy", None),
]

posts = [
    Post(1, "My mic is not workiing", "Some technical characters...", authors[0], date.today()),
    Post(2, "Need some help", "How can I open jar?", authors[1], date.today()),
    Post(3, "What is mean of life", None, authors[2], date.today()),
    Post(4, "XFCE not running after crash X11", "Some log from logfile", authors[0], date.today()),
    Post(5, "Keyboard not working after suspending", "My keyboard not working after suspending. Worls only after reboot.", authors[0], date.today()),
    Post(6, "Issue with dual monitor", "Black screen on second screen", authors[2], date.today()),
    Post(7, "How to turn off beep sound", "It is drives me crazy", authors[1], date.today()),
    Post(8, "Evolution on Gmail", "Cannot use Gmail with turned on two step auth", authors[1], date.today()),
    Post(9, "No internet after fresh install", "Installed new Archlinux and Wifi not works", authors[0], date.today()),
    Post(10, "Kernel panic after full upgrade", None, authors[0], date.today()),
]

def get_post_titles(request):
    return render(request, "forum.html", {"posts":posts})

def get_page(request,page):
    int(page)
    return render(request,"forum.html",{"page":page})

def get_name_and_date(request, name):
    return render(request,"forum.html",{"name":name,"today_date":timezone.now(),"numbers":[1,2,3]})

def get_post_id(request, id):
    return render(request, "post_id.html", {"post": posts[int(id)]})

"""def get_author_by_id(request,id):
    author = None
    for a in authors:
        if a.id ==id:
            author= a
            break
    return render(request, "authors.html", {"author": author})
"""
def get_author_by_id(request, id):
    return render(request, "authors.html", {"author", authors[int(id) -1]})