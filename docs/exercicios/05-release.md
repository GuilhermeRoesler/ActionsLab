# 05 — Criar um release versionado

## Objetivo

Ligar tag Git → validação → GitHub Release.

## Passos

1. Garanta que `main` está verde (CI + Security).
2. Crie e envie uma tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
3. Observe o workflow **Release**: ele roda lint/testes e cria a Release com notes.
4. Confira em **Releases** no GitHub.

## Critério de sucesso

- Existe uma Release `v1.0.0` gerada pelo workflow (não só pela UI manual).
- Você sabe quando usar tag vs deploy contínuo do Pages.
