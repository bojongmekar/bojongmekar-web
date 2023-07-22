from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from main.forms import FeedbackForm
from main.models import Feedback
from django.core import serializers

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    
    context = {
        'form': FeedbackForm()
    }
    return render(request, "home.html", context)

def show_json(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_feedback(request):  
    # create object of form
    form = FeedbackForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:index'))
    