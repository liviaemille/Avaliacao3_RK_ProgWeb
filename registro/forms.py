from dataclasses import field
from django import forms
from .models import Produto, Telefone

class ProdutoForm (forms.ModelForm):
    class Meta :
        model = Produto
        fields = ['pro_nome', 'pro_status', 'pro_doador']

class TelefoneForm (forms.ModelForm):
    class Meta :
        model = Telefone
        fields =['tel_telefone', 'tel_dono']