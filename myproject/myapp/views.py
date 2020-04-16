from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


def hello1(request):
   return render(request, "myapp/template/hello.html", {})


def hello2(request, number):
   text = "<h1>welcome to my app number %s!</h1>"% number
   return HttpResponse(text)