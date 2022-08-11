from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app1.forms import PersonForm

# Create your views here.
def index(request):
    return HttpResponse("Hello Django")
