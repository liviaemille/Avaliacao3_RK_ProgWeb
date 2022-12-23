from django.urls import path
#from .views import lista_produtos, novo_produto, editar_produto, deletar_produto
#from .views import tela_inicio, lista_telefones, novo_telefone, editar_telefone, deletar_telefone, opcoes_listagem
from . import views

urlpatterns = [
    path('', views.tela_inicio, name='tela_inicio'),
    path('opcoesbusca', views.opcoesbusca, name='opcoesbusca'),
    path('busca_telefone', views.busca_telefone, name='busca_telefone'),
    path('busca_produto', views.busca_produto, name='busca_produto'),
    path('listagens', views.opcoes_listagem, name='listagens'),
    path('listaprodutos', views.lista_produtos, name='lista_produtos'),
    path('novoproduto', views.novo_produto, name='novo_produto'),
    path('editarproduto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletarproduto/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('listatelefones', views.lista_telefones, name='lista_telefones'),
    path('novotelefone', views.novo_telefone, name='novo_telefone'),
    path('editartelefone/<int:id>/', views.editar_telefone, name='editar_telefone'),
    path('deletartelefone/<int:id>/', views.deletar_telefone, name='deletar_telefone'),
]