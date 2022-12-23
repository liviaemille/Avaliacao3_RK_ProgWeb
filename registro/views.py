from django.shortcuts import render, redirect
from .forms import ProdutoForm, TelefoneForm
from .models import Produto, Telefone
from django.views.generic import UpdateView

def tela_inicio (request):
    return render(request, 'crud/index.html')

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render (request, 'crud/produtos.html', {'produtos': produtos})

def novo_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'crud/form_produto.html', {'form': form})

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'crud/form_produto.html', {'form': form, 'produto': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'crud/confirmacaodelete.html', {'produto': produto })

def lista_telefones(request):
    telefones = Telefone.objects.all().order_by('dono')
    return render (request, 'crud/tabelatelefone.html', {'telefones': telefones })

def novo_telefone (request):
    form = TelefoneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_telefones')
    return render(request, 'crud/form_telefone.html', {'form': form})


def editar_telefone(request, id):
    telefone = Telefone.objects.get(id=id)
    form = TelefoneForm(request.POST or None, instance=telefone)

    if form.is_valid():
        form.save()
        return redirect('lista_telefones')
    return render(request, 'crud/form_telefone.html', {'form': form, 'telefone': telefone})


def deletar_telefone(request, id):
    telefone = Telefone.objects.get(id=id)
    
    if request.method == 'POST':
        telefone.delete()
        return redirect('lista_telefones')
    return render(request, 'crud/confirmacaodeletetel.html', {'telefone': telefone})

def opcoes_listagem(request):
    return render(request, 'crud/opcoeslistagem.html')

def opcoesbusca(request):
    return render(request, 'crud/opcoesbusca.html')

def busca_telefone(request):
    buscar = request.GET.get('buscatel',default="")
    telefones = Telefone.objects.filter(dono__icontains=buscar)
    return render(request, 'crud/buscatelefone.html', {'telefones': telefones})

def busca_produto(request):
    buscar = request.GET.get('buscapro', default="")    
    produtos = Produto.objects.filter(nome__icontains=buscar)
    return render(request, 'crud/buscaproduto.html', {'produtos': produtos})