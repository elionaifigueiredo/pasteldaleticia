from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import Pastel

# Create your views here.

def index(request):
    msg = "Ola Mundo Django"
    lista = Pastel.objects.all()
    return render(request, 'pastel/index.html', {'msg': msg, 'lista':lista})    
