from django.shortcuts import render

# Create your views here.

def umkm(request):
    return render(request, 'umkm.html')