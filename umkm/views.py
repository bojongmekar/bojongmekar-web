from django.http import HttpResponse
from django.shortcuts import render
from umkm.models import Product
from django.core import serializers

# Create your views here.

def umkm(request):
    produk = Product.objects.all()

    context = {
        'product_list': produk
    }
    return render(request, 'umkm.html', context)

def konten(request, pk):
    content = Product.objects.get(pk = pk)

    context = {
        'content': content
    }
    return render(request, 'konten-umkm.html', context)

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")