# 01 — Fazer o CI falhar (de propósito)

## Objetivo

Ver o ciclo completo de feedback: mudança → Actions vermelho → correção → verde.

## Passos

1. Crie uma branch `exercise/break-ci`.
2. Em `calculadora.py`, altere `somar` para retornar `a - b` (erro intencional).
3. Abra um Pull Request para `main`.
4. Observe o workflow **CI** falhar nos jobs da matrix.
5. Reverta a lógica, faça push e confirme o CI verde.

## Critério de sucesso

- Você consegue apontar, na UI do Actions, **qual step** falhou e **por quê**.
- O PR só fica mergeável (com branch protection) depois do verde.
