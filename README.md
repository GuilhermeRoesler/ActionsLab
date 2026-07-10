# CI na Prática

Projeto de exemplo para aprender Integração Contínua (CI) com GitHub Actions.

## Rodando manualmente (sem CI)

```bash
pip install -r requirements.txt
ruff check .
pytest --verbose
```

## Rodando com CI

Basta dar push (ou abrir um Pull Request) para o GitHub. O workflow em
`.github/workflows/ci.yml` roda automaticamente as mesmas etapas acima
em uma máquina do GitHub, sem você precisar fazer nada manualmente.

Veja o resultado na aba **Actions** do repositório.
