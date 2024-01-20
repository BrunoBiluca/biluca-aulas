import pytest
from testes_unitarios.main import area_triangulo


def test_area_deve_ser_quando_altura_e_base_validos():
    area = area_triangulo(base=3, altura=2)
    assert area == 3


def test_area_deve_ser_0_quando_altura_0():
    area = area_triangulo(base=3, altura=0)
    assert area == 0


def test_area_deve_ser_0_quando_base_0():
    area = area_triangulo(base=0, altura=3)
    assert area == 0


def test_area_deve_ser_quando_altura_e_base_quebrados():
    area = area_triangulo(base=2.4, altura=3.7)
    assert area == pytest.approx(4.44, 0.01)
