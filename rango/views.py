from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse









# def index(request):
#     return HttpResponse("rango says hey there world!")

def index(request):
    context_dict = {'boldmessage':"I am bold font from the context"}
    return render(request,'rango/index.html',context_dict)