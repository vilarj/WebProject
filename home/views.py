from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About me")