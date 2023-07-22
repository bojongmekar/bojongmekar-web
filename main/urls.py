from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('json/', show_json, name='show_json'),
    path('add/', add_feedback, name='add_feedback'),
]