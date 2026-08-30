"""
Módulo de demonstração (calculadora) usado como pretexto para o lab de CI/CD.

O valor pedagógico deste repositório está nos pipelines em `.github/workflows/`,
não na complexidade da lógica de negócio.
"""

from __future__ import annotations


def somar(a: float, b: float) -> float:
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de a por b."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de a e b."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna a divisão de a por b.

    Raises:
        ZeroDivisionError: se b for 0.
    """
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
