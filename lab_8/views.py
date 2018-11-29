from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
import urllib.request
import json
import requests
# Create your views here.

response = {}
def index(request):
    return render(request, 'home.html', response)

def login(request):
    return render(request, 'login.html', response)

def logout(request):
    logout_user(request)
    return redirect("index")

# def book_data(request):
#     try:
#         search = request.GET["search"]
#     except:
#         search = "quilting"
#     raw_data = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + search).json()
#     itemss = []
#     for info in raw_data['items']:
#         data = {}
#         data['title'] = info['volumeInfo']['title']
#         data['author'] = ", ".join(info['volumeInfo']['authors'])
#         data['publishedDate'] = info['volumeInfo']['publishedDate']
#         itemss.append(data)
#     return JsonResponse({"data": itemss})


def buku(request):
    search = "quilting"
    if request.GET["search"] != "":
        search = request.GET["search"]
    
    getBooksJson = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + search)
    jsonParsed = json.dumps(getBooksJson.json())
    return HttpResponse(jsonParsed)
