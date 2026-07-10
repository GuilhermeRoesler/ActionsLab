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

## Runner self-hosted

O job `local-check` roda em `runs-on: self-hosted`, ou seja, na sua
própria máquina, em vez de uma VM temporária do GitHub. Para isso
funcionar, você precisa ter o runner instalado e rodando localmente
(via `run.cmd` ou como serviço com `svc.cmd install` + `svc.cmd start`).

**Por que o `deploy` continua em `ubuntu-latest`?** As Actions oficiais
de GitHub Pages (`upload-pages-artifact`, `deploy-pages`) rodam scripts
internos em `bash`, e o `bash` do Git for Windows interpreta `\` como
caractere de escape — isso corrompe caminhos do Windows (que usam `\`)
e quebra a execução. É uma incompatibilidade conhecida dessas Actions
com runners Windows self-hosted, não um erro de configuração sua.
Por isso o `local-check` foi criado como um job separado, simples e
100% compatível com PowerShell, só para você ver o runner local em ação.

⚠️ Atenção: se o repositório for público, qualquer Pull Request de
terceiros pode potencialmente executar código na sua máquina. Para
este projeto de prática, prefira manter o repositório **privado**, ou
mantenha o runner restrito a jobs que só rodam em push direto na
`main` (como já está configurado aqui com `if: github.ref == ...`).

