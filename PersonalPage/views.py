from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "PersonalPage/home.html", {})

def about(request):
    return render(request, "PersonalPage/about.html", {})

def passion(request):
    return render(request, "PersonalPage/passion.html", {})
def contact(request):
    return render(request, "PersonalPage/contact.html", {})