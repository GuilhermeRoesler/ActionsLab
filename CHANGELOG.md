# Changelog pedagógico

Registro do que o laboratório passou a cobrir (foco em práticas de CI/CD, não em features da calculadora).

## 1.0.0 — Lab de portfólio

- Workflows separados: **CI**, **CD**, **Security**, **Release**
- Reusable workflow com **matrix** (Python 3.11/3.12, Ubuntu + Windows)
- Coverage gate (≥ 80%), JUnit/HTML **artifacts**
- Build **Docker** no CI (sem push de imagem)
- CD via `workflow_run` + environment **production** (GitHub Pages)
- **Dependabot** (pip + Actions), **pip-audit** e **CodeQL**
- Path filters, concurrency, `workflow_dispatch`
- Documentação: conceitos, glossário, branch protection, 5 exercícios
- App de demo tipado + testes parametrizados + `pyproject.toml`
- Self-hosted removido do caminho feliz (documentado como exercício opcional)
- LICENSE MIT, `.gitignore`, site didático no Pages
