from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Sched

# Create your views here.

response = {}

def index(request):
    return render(request, 'Website_Aji.html', response)

def schedule(request):
    response['schedl'] = Sched.objects.all().values()
    return render(request, "Schedule.html", response)

def addschedule(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['nama'] = request.POST['nama'] if request.POST['nama'] != "" else "Anonymous"
        response['tanggal'] = request.POST['tanggal']
        response['jam'] = request.POST['jam']
        response['tempat'] = request.POST['tempat']
        response['kategori'] = request.POST['kategori']
        message = Sched(nama=response['nama'], tanggal=response['tanggal'], jam=response['jam'],
                          tempat=response['tempat'], kategori=response['kategori'])
        message.save()
        schedule = Sched.objects.all()
        response['schedule'] = schedule
        html ='Schedule.html'
        return render(request, html, response)
    else:
        return HttpResponseRedirect('/lab-4/Schedule')

def InputForm(request):
    html = "addSched.html"
    response["sched"] = Message_Form
    return render(request, html, response)

def DeleteSched(request):
        schedule = Sched.objects.all().delete()
        response["schedule"] = schedule
        return render(request, "Schedule.html", response)
