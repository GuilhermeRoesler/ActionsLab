# Runner self-hosted (exercício opcional)

> **Não use self-hosted em repositório público** com PRs de terceiros.
> Qualquer workflow disparado por um PR pode executar código arbitrário **na sua máquina**.

Este laboratório **não** inclui job self-hosted nos workflows ativos de propósito:
em portfólio público, isso seria um risco, não um diferencial.

## Quando fazer este exercício

- Repositório **privado**, ou
- Runner restrito a `push` na `main` (nunca em `pull_request`), e
- Máquina dedicada / VM descartável (não o PC pessoal com dados sensíveis)

## Passos resumidos

1. No GitHub: **Settings → Actions → Runners → New self-hosted runner**
2. Siga as instruções do SO (Windows: `config.cmd` + `run.cmd`)
3. Adicione um workflow separado, por exemplo `.github/workflows/self-hosted-lab.yml`:

```yaml
name: Self-hosted lab
on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  local-check:
    if: github.event_name == 'push' || github.event_name == 'workflow_dispatch'
    runs-on: self-hosted
    steps:
      - uses: actions/checkout@v4
      - shell: pwsh
        run: |
          Write-Host "Host: $env:COMPUTERNAME"
          Write-Host "CWD: $PWD"
```

4. Confirme na aba **Actions** que o job aparece como `self-hosted`.

## Nota sobre GitHub Pages em Windows

Actions oficiais de Pages (`upload-pages-artifact`, `deploy-pages`) usam `bash` internamente e costumam falhar em runners Windows self-hosted por causa de caminhos com `\`. Mantenha o **deploy em `ubuntu-latest`** e use o self-hosted só para checks locais.
