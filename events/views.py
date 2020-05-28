from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'events/index4.html', context)