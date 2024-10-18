from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class ListaProdutos(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista produtos')


class DetalheProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe produtos')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
