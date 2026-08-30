# Glossário CI/CD (GitHub Actions)

| Termo | Significado curto |
|-------|-------------------|
| **CI** | Integração Contínua — build/lint/testes a cada mudança |
| **CD** | Entrega/Deploy Contínuo — publicar automaticamente após gates |
| **Workflow** | Arquivo YAML em `.github/workflows/` com um ou mais jobs |
| **Job** | Unidade que roda em um runner (`runs-on`) |
| **Step** | Passo dentro de um job (comando ou action) |
| **Runner** | Máquina que executa o job (`ubuntu-latest`, self-hosted, etc.) |
| **Matrix** | Estratégia que multiplica um job por combinações (versão, OS…) |
| **Artifact** | Arquivo gerado no job e armazenado temporariamente no GitHub |
| **Cache** | Reuso de dependências entre runs (ex.: pip) |
| **Environment** | Contexto de deploy (regras, URL, proteções) |
| **Gate** | Condição que impede o próximo estágio (ex.: `needs` + testes verdes) |
| **Path filter** | Limita quando o workflow dispara com base em arquivos alterados |
| **Concurrency** | Controla runs paralelos; pode cancelar o anterior da mesma branch |
| **Reusable workflow** | Workflow chamado por outro via `workflow_call` |
| **`workflow_dispatch`** | Disparo manual pela aba Actions |
| **`workflow_run`** | Disparo quando outro workflow termina |
| **Secret** | Credencial injetada no job sem aparecer no log |
| **Status check** | Resultado de um job exigido pela branch protection |
| **Dependabot** | Bots de PRs para atualizar dependências |
| **CodeQL** | Análise estática de segurança da GitHub |
