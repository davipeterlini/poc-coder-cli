# 🧠 CodeCLI

Uma aplicação de linha de comando (CLI) interativa que integra ferramentas Bash com inteligência artificial. Com suporte a múltiplos provedores (OpenAI, Claude, Gemini, Mistral, Ollama), edição de arquivos, planejamento de execução, histórico e comandos customizados.

## 📦 Funcionalidades

- CLI interativa com auto-completar
- Planejamento de execução com IA
- Edição de arquivos via comandos
- Execução de comandos Bash
- Suporte a múltiplos provedores de IA
- Configuração via arquivo `.yaml`
- Histórico de comandos e interações

## 🛠️ Requisitos

- Python 3.8+
- pip
- (opcional) [Ollama](https://ollama.com/) instalado para IA local

## 📥 Instalação

```bash
git clone https://github.com/seu-usuario/code_cli.git
cd code_cli_project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Configuração

Edite o arquivo `provider_config.yaml`:

```yaml
provider: ollama
model: llama3
endpoint: http://localhost:11434
api_key: null
max_tokens: 4096
temperature: 0.7
```

Você pode trocar o `provider` para `openai`, `claude`, `gemini`, etc.

## 🚀 Execução

Para iniciar o shell interativo:

```bash
python -m code_cli.main shell
```

## 🧪 Testes

```bash
pytest tests/
```

## 🧩 Extensões futuras

- Comandos `edit`, `plan`, `run`, `ai` e `provider`
- Templates e contexto para prompts
- Persistência de sessões

## 📄 Licença

MIT
