- 07/04/2025
  - Criação de Prompt - https://chatgpt.com/c/67f27ca5-fafc-8004-9e10-efd770c36b76
  - Verificar estrutura criada



codeai-cli/
├── codeai/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── planner.py
│   │   ├── editor.py
│   │   ├── executor.py
│   │   └── session.py
│   ├── providers/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── openai_provider.py
│   │   ├── ollama_provider.py
│   │   └── anthropic_provider.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── shell.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_config.py
├── .gitignore
├── config.yaml
├── README.md
└── requirements.txt