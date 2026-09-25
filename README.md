# AST07 — Selenium

Atividade da disciplina de **Automated Software Testing (AST)**, utilizando **Selenium WebDriver** e **Pytest** para automação de testes em uma página HTML.

## Tecnologias

- Python
- Selenium
- Pytest
- GitHub Actions

## Testes realizados

1. **Formulário** — preenchimento de nome e e-mail e validação da mensagem de sucesso.
2. **Ações de mouse** — duplo clique e clique com o botão direito.
3. **Ações de teclado** — seleção, exclusão e preenchimento do campo de observações.

## Estrutura

```text
AST07-Selenium/
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── portal.html
├── test_portal.py
├── requirements.txt
└── README.md
```

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest test_portal.py -v
```

### Resultado

Os 3 testes foram executados com sucesso:

```text
3 passed
```

O projeto também possui **CI com GitHub Actions**, que executa os testes automaticamente no repositório.
