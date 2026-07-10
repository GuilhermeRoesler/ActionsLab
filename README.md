# CI/CD na Prática

Projeto de exemplo para aprender Integração Contínua (CI) e Entrega/Deploy
Contínuo (CD) com GitHub Actions.

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

## CD: deploy automático

Além dos testes, o workflow tem um segundo job (`deploy`) que só roda
**depois** que o job `test` passa (`needs: test`), e só quando o push é
direto na branch `main`. Esse job publica o conteúdo da pasta `site/`
no GitHub Pages — sem nenhuma ação manual.

Para habilitar (só precisa fazer uma vez):
1. No repositório, vá em **Settings → Pages**
2. Em "Build and deployment" → "Source", selecione **GitHub Actions**
3. Dê push na `main` — o Pages será publicado automaticamente

A URL final aparece em **Settings → Pages** e também no resumo da
execução, na aba Actions (job `deploy`).

