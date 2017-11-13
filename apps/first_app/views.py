from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Placeholder to later display all the lists of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder to display blog {}".format(number)
    return HttpResponse(response)

def edit(request):
    response = "Placeholder to edit blog {{number}}"
    return HttpResponse(response)

def destroy(request):
    return redirect('/')