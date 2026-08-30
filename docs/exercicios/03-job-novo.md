# 03 — Adicionar um job novo no CI

## Objetivo

Praticar composição de pipeline: novo job, dependência (`needs`) e artifact.

## Passos

1. Em `ci.yml`, adicione um job `sbom` (ou `pip-freeze`) que:
   - `needs: quality`
   - gera um arquivo `deps.txt` com `pip freeze`
   - faz upload com `actions/upload-artifact@v4`
2. Dispare via `workflow_dispatch` ou push.
3. Baixe o artifact na UI do Actions.

## Critério de sucesso

- O job só roda se a matrix de testes passou.
- O artifact aparece na execução com retenção configurada.
