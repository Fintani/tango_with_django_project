from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    #dictionary what to put in the template
    context_dict = {"boldmessage" : "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, "rango/index.html", context=context_dict)

def about(request):
    return render(request, "rango/about.html")
