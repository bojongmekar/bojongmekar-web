from django.urls import path
from umkm.views import *

app_name = 'umkm'

urlpatterns = [
    path('', umkm, name='umkm'),
    path('json/', show_json, name='show_json'),
    path('konten/<int:pk>/', konten, name='konten')
]