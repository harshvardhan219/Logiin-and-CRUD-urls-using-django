from django.shortcuts import render

# Create your views here.
def signup(request):
    context={}
    return render(request, "loginpart/signup.html",context)
def login(request):
    context={}
    return render(request, "loginpart/login.html",context)