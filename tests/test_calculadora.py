"""
Testes parametrizados da calculadora de demonstração.

Rodar localmente:
  pip install -r requirements.txt
  pytest --cov=calculadora --cov-report=term-missing
"""

from __future__ import annotations

import pytest

from calculadora import dividir, multiplicar, somar, subtrair


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_somar(a: float, b: float, esperado: float) -> None:
    assert somar(a, b) == esperado


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (5, 3, 2),
        (0, 5, -5),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtrair(a: float, b: float, esperado: float) -> None:
    assert subtrair(a, b) == esperado


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (4, 3, 12),
        (-2, 3, -6),
        (2.5, 2, 5.0),
    ],
)
def test_multiplicar(a: float, b: float, esperado: float) -> None:
    assert multiplicar(a, b) == esperado


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-8, 4, -2),
    ],
)
def test_dividir(a: float, b: float, esperado: float) -> None:
    assert dividir(a, b) == esperado


def test_dividir_por_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="zero"):
        dividir(10, 0)
