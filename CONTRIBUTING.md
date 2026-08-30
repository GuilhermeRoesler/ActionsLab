# Contribuindo

Obrigado por contribuir com este laboratório de CI/CD.

## Fluxo sugerido

1. Faça um **fork** do repositório (ou clone, se tiver acesso).
2. Crie uma branch descritiva:
   ```bash
   git checkout -b feat/meu-exercicio
   ```
3. Instale as dependências e rode a suíte localmente:
   ```bash
   pip install -r requirements.txt
   ruff check .
   pytest --cov=calculadora --cov-fail-under=80
   ```
4. Abra um **Pull Request** para `main`.
5. Acompanhe a aba **Actions**: os workflows `CI` e `Security` devem rodar no PR.
6. O deploy (`CD — GitHub Pages`) só ocorre após CI verde em `main`.

## O que é bem-vindo

- Novos exercícios em `docs/exercicios/`
- Melhorias nos workflows (comentadas e documentadas)
- Correções de typos / clareza no README
- Atualizações de dependências via Dependabot

## O que evitar

- Commits que quebrem a suíte sem propósito pedagógico documentado
- Adicionar runner **self-hosted** em forks públicos (veja `docs/self-hosted-opcional.md`)
- Secrets reais no repositório

## Padrão de commit

Prefira mensagens curtas focadas no *porquê*:

- `feat: adiciona job de coverage no CI`
- `docs: explica matrix no glossário`
- `fix: corrige path filter do CD`
