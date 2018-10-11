from django.shortcuts import render
from .forms import add_status
from .models import Statuy
from django.http import HttpResponseRedirect

# Create your views here.
response = {}
def index(request):
    return render(request,'status.html', response)

def profile(request):
    return render(request,'profile.html', response)

def addStatus(request):
    if (request.method == 'POST'):
        forms = add_status(request.POST)
        if (forms.is_valid()):
            statuz = forms.save(commit=True)
            statuz.save()
        return HttpResponseRedirect('/lab-6/status')
    else:
        forms = add_status()
        isiStatus = Statuy.objects.all()
        context = {
            'stats' : isiStatus,
        }
    return render(request, 'status.html', { 'form' : forms, 'stats' : isiStatus} )

def DeleteStatus(request):
    Statuy.objects.all().delete()
    return HttpResponseRedirect('/lab-6/status')
