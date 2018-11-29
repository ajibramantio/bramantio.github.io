from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Create your views here.
response = {}
def indexlab11(request):
	return render(request, 'login.html')

def index(request):
    if request.user.is_authenticated and "like" not in request.session:
        request.session["fullname"] = request.user.first_name + \
            " "+request.user.last_name
        request.session["username"] = request.user.username
        request.session["email"] = request.user.email
        request.session["sessionid"] = request.session.session_key
        request.session["like"] = []
    return render(request, 'book.html')
# return render(request,'booklist.html')

@csrf_exempt
def like(request):
    if(request.method == "POST"):
        lst = request.session["like"]
        if request.POST["id"] not in lst:
            lst.append(request.POST["id"])
        print(request.session["sessionid"])
        print(request.session["like"])
        request.session["like"] = lst
        response["message"] = len(lst)
        return JsonResponse(response)
    else:
        return HttpResponse("GET Method not allowed")

@csrf_exempt
def unlike(request):
    if(request.method == "POST"):
        lst = request.session["like"]
        if request.POST["id"] in lst:
            lst.remove(request.POST["id"])
        print(request.session["sessionid"])
        print(request.session["like"])
        request.session["like"] = lst
        response["message"] = len(lst)
        return JsonResponse(response)
    else:
        return HttpResponse("GET Method not allowed")

def get_like(request):
    if request.user.is_authenticated:
        if(request.method == "GET"):
            if request.session["like"] is not None:
                response["message"] = request.session["like"]
        else:
            response["message"] = "NOT ALLOWED"
    else:
        response["message"] = ""
    return JsonResponse(response)

def booklist(request):
	try:
		q = request.GET['q']
	except:
		q = 'quilting'

	json_read = requests.get(
		'https://www.googleapis.com/books/v1/volumes?q=' + q).json()
	return JsonResponse(json_read)
