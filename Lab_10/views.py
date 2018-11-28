from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormSubscribe, subs_form
from .models import Subscriber

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def subscribe(request):
    form = FormSubscribe(request.POST)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        status_subscribe = True
        try:
            Subscriber.objects.create(**data)
        except:
            status_subscribe = False
        return JsonResponse({'status_subscribe': status_subscribe})
    content = {'form': form}
    return render(request, 'subscribe.html', content)

def checkEmail(request):
    if request.method == "POST":
        email = request.POST['email']
        is_email_already_exist = Subscriber.objects.filter(pk=email).exists()
        return JsonResponse({'is_email': is_email_already_exist})

def getSubscribers(request):
    if request.method == 'POST':
        dataSubscribe = Subscriber.objects.all().values()
        Subscribers = list(dataSubscribe)
        return JsonResponse({'Subscribers': Subscribers})

@csrf_exempt
def Subscribe_Views(request):
	all_subs = Subscriber.objects.all()
	subs_list = Subscriber.objects.all()
	if request.method == "POST":
		form = subs_form(request.POST)
		if form.is_valid():
			form_item = form.save(commit=True)
			form_item.save()
			form = subs_form()
	else:
		form = subs_form()

	return render(request, 'subs.html', {'form': form, 'subs_list': subs_list})

def subs_list(request):
    subs_list = Subscriber.objects.all()
    response['subs_list'] = subs_list
    html = 'subs.html'
    return render(request, html, response)


def subs_list_json(request):  # update
    subs = [obj.as_dict() for obj in Subscriber.objects.all()]
    return JsonResponse({"results": subs}, content_type='application/json')


@csrf_exempt
def unsubscribe(request):
	if request.method == "POST":
		email = request.POST['email']
		Subscriber.objects.filter(email=email).delete()
		return HttpResponseRedirect('/Lab_10/')
