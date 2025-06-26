from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse("hi there! Im django developer")
    return render(request, 'about.html')
def home(request):
    #return HttpResponse("hi there! Im django developer")
    return render(request, 'home.html')