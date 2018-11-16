from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import urllib.request
import json
import requests
# Create your views here.

response = {}
def index(request):
    return render(request, 'home.html', response)

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
    try:
        search = request.GET["search"]
    except:
        search = "quilting"

    getBooksJson = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + search)
    jsonParsed = json.dumps(getBooksJson.json())
    return HttpResponse(jsonParsed)