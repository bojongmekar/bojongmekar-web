from django.shortcuts import render

# Create your views here.

def artikel(request):
    return render(request, "artikel.html")