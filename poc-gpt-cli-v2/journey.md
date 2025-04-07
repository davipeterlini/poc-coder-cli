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