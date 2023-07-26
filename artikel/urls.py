from django.urls import path
from artikel.views import *

app_name = 'artikel'

urlpatterns = [
    path('', artikel, name='artikel'),
    path('json/', show_json, name='show_json'),
    path('konten/<int:pk>/', konten, name='konten')
]