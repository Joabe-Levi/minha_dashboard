import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Vendas, Produto, Vendedor
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime


class Home(TemplateView):
    template_name = 'home.html'


class RetornaTotalVendido(View):

    def get(self, request, *args, **kwargs):
        total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
        return JsonResponse({'total': total})


class RelatorioFaturamento(View):
    def get(self, request, *args, **kwargs):
        x = Vendas.objects.all()

        meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
        data = []
        labels = []
        cont = 0
        mes = datetime.now().month + 1
        ano = datetime.now().year
        for i in range(12):
            mes -= 1
            if mes == 0:
                mes = 12
                ano -= 1

            y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
            labels.append(meses[mes - 1])
            data.append(y)
            cont += 1

        data_json = {'data': data[::-1], 'labels': labels[::-1]}

        return JsonResponse(data_json)


class RelatorioProdutos(View):
    def get(self, request, *args, **kwargs):
        return self.relatorio_produtos()

    def relatorio_produtos(self):
        produtos = Produto.objects.all()
        label = []
        data = []
        for produto in produtos:
            vendas = Vendas.objects.filter(nome_produto=produto).aggregate(Sum('total'))
            if not vendas['total__sum']:
                vendas['total__sum'] = 0
            label.append(produto.nome)
            data.append(vendas['total__sum'])

        x = list(zip(label, data))
        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))

        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})


class RelatorioFuncionario(View):

    def get(self, request, *args, **kwargs):
        return self.relatorio_funcionario()

    def relatorio_funcionario(self):
        vendedores = Vendedor.objects.all()
        label = []
        data = []
        for vendedor in vendedores:
            vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
            if not vendas['total__sum']:
                vendas['total__sum'] = 0
            label.append(vendedor.nome)
            data.append(vendas['total__sum'])

        x = list(zip(label, data))
        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))

        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})