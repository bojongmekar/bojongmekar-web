from django.shortcuts import render

# Create your views here.

def sejarah(request):
    return render(request, "sejarah.html")

def wilayah(request):
    return render(request, "wilayah.html")

def potensi(request):
    return render(request, "potensi.html")

def masyarakat(request):
    return render(request, "masyarakat.html")