
from django import forms       
from .models import Pastel
            

class PastelForm(forms.ModelForm):
    class Meta:
        model = Pastel
        fields = ('nome','quantidade','descricao','preco','foto') 