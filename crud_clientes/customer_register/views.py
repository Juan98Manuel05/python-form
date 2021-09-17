from django.shortcuts import render, redirect
from .forms import customerForm
from .models import customer

from .forms import requestsForm
from .models import requests

# Create your views here.

def customer_list(request):
    context = {'customer_list': customer.objects.all()}
    return render(request, "customer_register/customer_list.html", context)

def customer_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = customerForm()
        else:
            custom = customer.objects.get(pk = id)
            form = customerForm( instance = custom )
        return render(request, "customer_register/customer_form.html", {'form': form})
    else:
        if id == 0:
            form = customerForm(request.POST)
        else:
            custom = customer.objects.get(pk = id)
            form = customerForm(request.POST, instance = custom)
        if form.is_valid():
            form.save()
        return redirect('/customer/list')

def customer_delete(request, id):
    custom = customer.objects.get(pk = id)
    custom.delete()
    return redirect('/customer/list')




def request_list(request):
    context = {'customer_list': requests.objects.all()}
    return render(request, "ejercicio/list.html", context)

def request_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = customerForm()
        else:
            custom = requests.objects.get(pk = id)
            form = customerForm( instance = custom )
        return render(request, "ejercicio/form.html", {'form': form})
    else:
        if id == 0:
            form = customerForm(request.POST)
        else:
            custom = requests.objects.get(pk = id)
            form = customerForm(request.POST, instance = custom)
        if form.is_valid():
            form.save()
        return redirect('/customer/list')


def request_delete(request, id):
    custom = requests.objects.get(pk = id)
    custom.delete()
    return redirect('/customer/list')

