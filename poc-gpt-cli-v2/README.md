Claro! Aqui está um `README.md` completo para o projeto **CodeAI CLI**, incluindo instruções de instalação, uso e configuração dos providers de IA:

---

```markdown
# 🤖 CodeAI CLI

**CodeAI CLI** é um copiloto de código no terminal, feito em Python, com suporte a múltiplos provedores de modelos de linguagem (LLMs), incluindo OpenAI, Anthropic, e modelos locais via Ollama. A interface é 100% em linha de comando e permite executar interações com IA, edição de código, planejamento e ferramentas Bash integradas.

---

## 🚀 Funcionalidades

- ✅ Suporte a múltiplos providers de IA (OpenAI, Anthropic, Ollama/local)
- 🛠️ Ferramentas de edição de código com IA
- 💬 CLI interativa para prompts e sessões
- 📋 Planejador de execução para organização de tarefas
- 💻 Integração com ferramentas de shell/Bash
- 📂 Arquivo de configuração centralizado (`config.yaml`)

---

## 🧱 Estrutura do Projeto

```
codeai-cli/
│
├── codeai/
│   ├── cli.py               # Entrypoint CLI (Typer)
│   ├── main.py              # Execução principal
│   ├── config.py            # Loader de configuração dos providers
│   └── providers/           # Implementações dos providers (OpenAI, Ollama, Anthropic)
│
├── config.yaml              # Arquivo de configuração de providers
├── requirements.txt         # Dependências do projeto
├── README.md                # Este arquivo
└── tests/                   # Testes automatizados
```

---

## 🧪 Requisitos

- Python 3.9+
- Acesso à API dos providers desejados (ex: OpenAI, Anthropic)
- Opcional: [Ollama](https://ollama.com) instalado localmente para uso de LLMs offline

---

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/codeai-cli.git
cd codeai-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🧬 Configuração

Edite o arquivo `config.yaml` com suas chaves e modelos preferidos:

```yaml
default_provider: openai

providers:
  openai:
    api_key: ENV:OPENAI_API_KEY
    model: gpt-4

  ollama:
    endpoint: http://localhost:11434
    model: codellama

  anthropic:
    api_key: ENV:CLAUDE_API_KEY
    model: claude-3-sonnet
```

Crie um arquivo `.env` (opcional) com suas variáveis de ambiente:

```env
OPENAI_API_KEY=sk-...
CLAUDE_API_KEY=sk-ant-...
```

---

## 🧠 Como Usar

### Fazer uma pergunta à IA:

```bash
python codeai/main.py ask "Explique o padrão Observer em Python"
```

### Rodar no modo CLI interativo (em breve):

```bash
python codeai/main.py
```

---

## 🔌 Providers Suportados

| Provider   | Suporte | Observações |
|------------|---------|-------------|
| OpenAI     | ✅       | via `api_key` |
| Anthropic  | ✅       | via `Claude` |
| Ollama     | ✅       | local, sem internet |

---

## 📄 Licença

MIT © 2025 - Desenvolvido por [Seu Nome]

---

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

```

Se quiser, posso ajustar o conteúdo com base em seu nome, repositório real ou adicionar badges do GitHub. Deseja isso?