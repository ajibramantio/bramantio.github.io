from django.shortcuts import render

# Create your views here.

response = {}
def index(request):
    return render(request, 'home.html', response)
