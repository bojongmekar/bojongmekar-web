from django.urls import path
from artikel.views import *

app_name = 'artikel'

urlpatterns = [
    path('', artikel, name='artikel'),
]