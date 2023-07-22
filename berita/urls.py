from django.urls import path
from berita.views import *

app_name = 'berita'

urlpatterns = [
    path('', berita, name='berita'),
    path('json/', show_json, name='show_json'),
    path('konten/<int:pk>/', konten, name='konten')
]