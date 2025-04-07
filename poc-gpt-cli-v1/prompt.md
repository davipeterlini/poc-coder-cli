
### **Goal (Meta)**  
Crie uma aplicação **CLI interativa em Python**, inspirada no Code Claude, que funcione como um copiloto de desenvolvimento, integrando múltiplos modelos de linguagem (remotos e locais) para explicar, editar, planejar e executar tarefas com base no código do usuário. A aplicação deve ser extensível, segura e adaptável a diferentes fluxos de trabalho em projetos de software.

---

### **Return Format (Formato de Retorno)**  
A aplicação deve incluir:

#### **1. CLI Interativa (REPL ou modo shell):**
- Comandos como `ask`, `edit`, `explain`, `summarize`, `plan`, `run`, `commit`, `history`.
- Menu de ajuda (`--help`) com descrição dos comandos.
- Suporte a autocompletar e histórico de comandos.

#### **2. Módulo de Provedores de IA:**
- Sistema unificado de providers com suporte a:
  - **OpenAI (GPT-4, GPT-3.5)**
  - **Anthropic (Claude)**
  - **Google (Gemini)**
  - **Mistral**
  - **Ollama local (com modelos como `llama2`, `codellama`, `mistral`, etc)**

- Providers e modelos devem ser definidos em **`config.yaml`**:
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

#### **3. Edit Tools:**
- Comando `edit <arquivo>` com sugestões da IA aplicadas com confirmação.
- Operações inline: "trocar função", "mover bloco", "renomear variável", etc.
- Integração com Git para rastrear e reverter alterações.

#### **4. Bash Tools:**
- Comando `run <script.sh>` com sandbox opcional.
- Execução explicada (`explain run.sh`) com análise da IA.
- Aviso antes da execução real (modo seguro com confirmação).

#### **5. Planejador de Execução:**
- Comando `plan <objetivo>` para gerar plano de ação com etapas numeradas.
- Gerenciador de tarefas com `done`, `skip`, `retry`, `add`.
- Armazenamento e reuso de planos anteriores.

#### **6. Arquitetura Técnica (Python):**
- Estrutura modular em Python, usando:
  - `Click` ou `Typer` para CLI
  - `httpx` para requisições HTTP
  - `rich` ou `prompt_toolkit` para terminal interativo colorido
  - `pydantic` para validação do arquivo de configuração
- Sistema de providers pluggável via interface (`BaseProvider`)

---

### **Warnings (Avisos)**  
- Nenhuma interface gráfica: **terminal apenas**.  
- Toda execução de comandos shell precisa de confirmação do usuário.  
- Evite armazenar código do usuário em logs sem consentimento.  
- A aplicação precisa funcionar em Unix/macOS/Windows.  
- O config deve suportar variáveis de ambiente para chaves de API.  
- Limites de contexto/token devem ser tratados por provider.

---

### **Context Dump (Contexto adicional)**  
A aplicação será usada por desenvolvedores em ambientes locais e em times. Eles desejam total controle sobre a IA usada (por isso o suporte ao **Ollama** e outros providers externos), com capacidade de alternar entre modelos conforme o caso.  
A ferramenta deve funcionar offline com modelos locais e online com APIs, sendo altamente extensível e fácil de configurar.  
O foco está em produtividade, automação de tarefas de engenharia, e integração nativa com fluxo de trabalho Git/Bash.  
O estilo de uso é semelhante a um shell: comandos curtos, respostas claras, ações rápidas.

---