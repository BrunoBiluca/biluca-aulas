import pytest
from Exercício import abrir_arquivo,quebra_linha


def test_abrir_arquivos():
    linhas_arquivo = abrir_arquivo('controle_financeiro.csv')
    assert len(linhas_arquivo) == 8

def test_quebra_linha():
    quebra_linhas = quebra_linha(['gato,23','bruno,45','felps,22','layne,18'])
    assert len(quebra_linhas)== 4
    assert quebra_linhas[0] == ['gato','23']