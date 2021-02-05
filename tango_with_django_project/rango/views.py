from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Rango says hey there partner... no it doesnt haha i am pleb!")
