from dataclasses import field
from django import forms
from .models import Produto, Telefone

class ProdutoForm (forms.ModelForm):
    class Meta :
        model = Produto
        fields = ['nome', 'status', 'doador']

class TelefoneForm (forms.ModelForm):
    class Meta :
        model = Telefone
        fields =['telefone', 'dono']