from django.urls import path
from umkm.views import *

app_name = 'umkm'

urlpatterns = [
    path('', umkm, name='umkm'),
]