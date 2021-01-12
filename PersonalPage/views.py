from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "PersonalPage/home.html", {})

# def about(request):
#     return render(request, "PersonalPage/templates/about.html", {})
#
# def passion(request):
#     return render(request, "PersonalPage/templates/passion.html", {})
