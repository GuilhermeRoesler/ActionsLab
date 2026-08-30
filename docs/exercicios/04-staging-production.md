# 04 — Staging vs production

## Objetivo

Separar **validação** de **publicação** com environments.

## Passos

1. Em **Settings → Environments**, crie `staging` e confirme que `github-pages` existe.
2. No `cd.yml`, adicione um job `deploy-staging` que:
   - roda em `pull_request`
   - usa `environment: staging`
   - apenas faz upload do artifact do `site/` **sem** chamar `deploy-pages` (simula preview)
3. Mantenha o job atual de Pages só em `github-pages` / `main`.
4. Documente no README a diferença entre os dois environments.

## Critério de sucesso

- PR exerce staging; merge na `main` exerce o environment de Pages.
- Você consegue explicar por que preview ≠ produção.
