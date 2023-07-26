from django.http import HttpResponse
from django.shortcuts import render
from artikel.models import Article
from django.core import serializers

# Create your views here.

def artikel(request):
    articles = Article.objects.all()

    context = {
        'article_list': articles
    }
    return render(request, 'artikel.html', context)

def konten(request, pk):
    content = Article.objects.get(pk = pk)

    context = {
        'content': content
    }
    return render(request, 'konten-artikel.html', context)

def show_json(request):
    data = Article.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")