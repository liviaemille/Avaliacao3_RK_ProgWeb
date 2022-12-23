from sys import maxsize
from tabnanny import verbose
from django.db import models

# Create your models here.
class Produto (models.Model):
    STATUS_CHOICES = (
        ("Em estoque", "Disponível"),
        ("Doado", "Doado")
    )
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Produto')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, blank=False, null=False, verbose_name='Status')
    doador = models.CharField(max_length=100, null=False, blank=False, verbose_name='Doador')

    def __str__(self):
        return self.pro_nome

class Telefone (models.Model):
    telefone = models.CharField(max_length=11, null=False, blank=False, verbose_name='Telefone')
    dono = models.CharField(max_length=100, null=False, blank=False, verbose_name='Dono')

    def __str__(self):
        return self.tel_telefone