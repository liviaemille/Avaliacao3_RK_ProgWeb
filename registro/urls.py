from django.urls import path
from .views import lista_produtos, novo_produto, editar_produto, deletar_produto
from .views import tela_inicio, lista_telefones, novo_telefone, editar_telefone, deletar_telefone

urlpatterns = [
    path('', tela_inicio, name='tela_inicio'),
    path('listaprodutos', lista_produtos, name='lista_produtos'),
    path('novoproduto', novo_produto, name='novo_produto'),
    path('editarproduto/<int:id>/', editar_produto, name='editar_produto'),
    path('deletarproduto/<int:id>/', deletar_produto, name='deletar_produto'),
    path('listatelefones', lista_telefones, name='lista_telefones'),
    path('novotelefone', novo_telefone, name='novo_telefone'),
    path('editartelefone/<int:id>/', editar_telefone, name='editar_telefone'),
    path('deletartelefone/<int:id>/', deletar_telefone, name='deletar_telefone'),
]