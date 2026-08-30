# Branch protection (checklist)

Em um repositório de portfólio/equipe, proteja `main` para que só entre código validado pelo CI.

## Configuração recomendada (GitHub UI)

1. **Settings → Branches → Add branch protection rule**
2. Branch name pattern: `main`
3. Ative:
   - **Require a pull request before merging**
   - **Require status checks to pass before merging**
   - Checks sugeridos (após o primeiro run aparecerem na lista):
     - `Lint & test (Python 3.11 / ubuntu-latest)`
     - `Lint & test (Python 3.12 / ubuntu-latest)`
     - `Lint & test (Python 3.12 / windows-latest)`
     - `Build image (Docker)`
     - `pip-audit (deps)` (opcional, se quiser security no gate)
   - **Require branches to be up to date before merging**
4. Em repositórios solo de estudo, você pode relaxar “require PR” — mas manter **required checks** já demonstra maturidade.

## Environments

O workflow de CD usa o environment `production`:

1. **Settings → Environments → New environment** → nome `production`
2. (Opcional) adicione **required reviewers** para simular aprovação humana antes do deploy
3. Em **Settings → Pages**, source = **GitHub Actions**

## Por que isso importa no portfólio

Branch protection + required checks mostram que você não só “tem um YAML”, mas entende **governança do pipeline**: nada vai para produção sem evidência automática.
