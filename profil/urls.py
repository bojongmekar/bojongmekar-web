from django.urls import path
from profil.views import *

app_name = 'profil'

urlpatterns = [
    path('sejarah/', sejarah, name='sejarah'),
    path('masyarakat/', masyarakat, name='masyarakat'),
    path('potensi/', potensi, name='potensi'),
    path('wilayah/', wilayah, name='wilayah'),
]