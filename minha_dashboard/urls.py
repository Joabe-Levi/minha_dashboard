from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('total_vendido/', views.RetornaTotalVendido.as_view(), name='retorna-total-vendido'),
    path('relatorio_faturamento/', views.RelatorioFaturamento.as_view(), name='relatorio-faturamento'),
    path('relatorio_produtos/', views.RelatorioProdutos.as_view(), name='relatorio-produto'),
    path('relatorio_funcionario/', views.RelatorioFuncionario.as_view(), name='relatorio-funcionario')
]