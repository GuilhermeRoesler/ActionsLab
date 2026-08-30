# 02 — Subir o coverage gate

## Objetivo

Entender coverage como **gate** de qualidade, não só como métrica.

## Passos

1. No `pyproject.toml`, em `[tool.coverage.report]`, mude `fail_under` de `80` para `95`.
2. No `reusable-test.yml`, alinhe `--cov-fail-under=95`.
3. Rode localmente: `pytest --cov=calculadora --cov-fail-under=95`.
4. Se passar fácil, adicione uma função nova **sem teste** e veja o CI falhar.
5. Cubra a função com testes e recupere o verde.

## Critério de sucesso

- Explicar a diferença entre “gerar relatório de coverage” e “falhar o job se estiver baixo”.
