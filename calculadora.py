"""
Módulo simples de calculadora, criado para praticar CI no GitHub.
"""


def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de a por b."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b. Lança ZeroDivisionError se b for 0."""
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
