from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.

def index(request):
    msg = "Ola Mundo Django"
    return render(request, 'pastel/index.html', {'msg': msg})    
