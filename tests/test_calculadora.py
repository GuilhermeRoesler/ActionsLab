"""
Testes para o módulo calculadora.
Rodar localmente com: pytest
"""

import pytest
from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0


def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 5) == -5


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
