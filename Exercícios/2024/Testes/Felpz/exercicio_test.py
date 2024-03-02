import pytest
from ControleFinanceiro import abrir_arquivo, quebra_linha

def test_abrir_arquivo():
    linas_arquivo = abrir_arquivo("controle_financeiro.csv")
    assert len(linas_arquivo) == 8
 
def test_quebra_linha():
    quebra_linhas = quebra_linha(['gato,23','eu,20'])
    assert len(quebra_linhas) == 2
    assert quebra_linhas[0] == ['gato','23']