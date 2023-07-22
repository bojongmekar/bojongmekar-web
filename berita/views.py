from django.http import HttpResponse
from django.shortcuts import render
from berita.models import News
from django.core import serializers

# Create your views here.

def berita(request):
    news = News.objects.all()

    context = {
        'news_list': news
    }
    return render(request, 'berita.html', context)

def konten(request, pk):
    content = News.objects.get(pk = pk)

    context = {
        'content': content
    }
    return render(request, 'konten.html', context)

def show_json(request):
    data = News.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")