from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('total_vendido/', views.retorna_total_vendido, name='retorna-total-vendido'),
    path('relatorio_faturamento/', views.relatorio_faturamento, name='relatorio-faturamento'),
    path('relatorio_produtos/', views.relatorio_produtos, name='relatorio-produto'),
    path('relatorio_funcionario/', views.relatorio_funcionario, name='relatorio-funcionario')
]