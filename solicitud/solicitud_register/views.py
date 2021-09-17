from django.shortcuts import render, redirect
from .forms import RequestForm
from .models import Requests

# Create your views here.
def requests_list(request):
    context = {'request_list': Requests.objects.all()}
    return render(request, "solicitud_register/request_list.html", context)

def request_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = RequestForm()
        else:
            req = Requests.objects.get(pk = id)
            form = RequestForm( instance = req )
        return render(request, "solicitud_register/request_form.html", { 'form': form })
    else:
        if id == 0:
            form = RequestForm(request.POST)
        else:
            req = Requests.objects.get(pk = id)
            form = RequestForm(request.POST, instance = req)
        if form.is_valid():
            form.save()
        return redirect('/request/list')

def requests_delete(request, id):
    req = Requests.objects.get(pk = id)
    req.delete()
    return redirect('/request/list')