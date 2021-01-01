from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import *

from .models import Pastel

# Create your views here.

def index(request):
    msg = "Ola Mundo Django"
    
    lista = Pastel.objects.all()
    return render(request, 'pastel/index.html', {'msg': msg, 'lista':lista})   


def post_new(request):
     if request.method == "POST":
         form = PastelForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PastelForm()
     return render(request, 'pastel/post_edit.html', {'form': form})
 
 


  
