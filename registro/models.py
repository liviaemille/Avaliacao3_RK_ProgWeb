from sys import maxsize
from tabnanny import verbose
from django.db import models

# Create your models here.
class Produto (models.Model):
    STATUS_CHOICES = (
        ("OK", "Disponível"),
        ("-", "Recebido")
    )
    pro_nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Produto')
    pro_status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=False, null=False, verbose_name='Status')
    pro_doador = models.CharField(max_length=100, null=False, blank=False, verbose_name='Doador')

    def __str__(self):
        return self.pro_nome

class Telefone (models.Model):
    tel_telefone = models.CharField(max_length=11, null=False, blank=False, verbose_name='Telefone')
    tel_dono = models.CharField(max_length=100, null=False, blank=False, verbose_name='Dono')

    def __str__(self):
        return self.tel_telefone