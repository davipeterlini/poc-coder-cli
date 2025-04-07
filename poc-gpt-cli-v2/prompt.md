
---

### **Goal**

Quero construir uma aplicação CLI interativa em **Python**, inspirada no Code Claude, que permita ao usuário navegar por arquivos, editar, executar código e interagir com uma IA para geração, explicação, planejamento e refatoração de código. A aplicação deve suportar **múltiplos provedores de IA** (como OpenAI, Claude, Gemini, Mistral, Ollama), definidos via **arquivo de configuração local**, e manter todo o histórico e contexto das interações.

---

### **Return Format**

Retorne os seguintes componentes, com nível técnico suficiente para iniciar o desenvolvimento imediato:

1. **Visão Geral**  
   Descrição da aplicação, público-alvo e diferenciais.

2. **Arquitetura Técnica**  
   Estrutura dos módulos principais da aplicação, com destaque para:
   - CLI com Typer e Prompt Toolkit  
   - Gerenciador de provedores de IA  
   - Configuração local com arquivo `.yaml`  
   - Camadas de execução de código, edição, histórico, etc.

3. **Componentes Detalhados**  
   - **Interactive CLI Shell** com comandos: `cd`, `ls`, `open`, `edit`, `run`, `ai`, `plan`, `git`, `config`, `history`, `provider`  
   - **Editor embutido ou externo** para manipulação de arquivos com IA  
   - **IA Wrapper Abstrato**, com suporte a múltiplos providers (OpenAI, Claude, Gemini, Mistral, Ollama)  
   - **Execution Planner**, com comandos como `plan` e `run plan`  
   - **Ferramentas Bash** com interceptação inteligente  
   - **Histórico e Sessões** com persistência  
   - **Sistema de Configuração** para provider, modelo, endpoint, token, temperatura, etc.

4. **Exemplos de Uso**  
   Demonstrações de como um desenvolvedor usaria a ferramenta passo a passo com comandos reais

---

### **Warnings**

- A execução de código precisa ser isolada (ex.: Docker)  
- IA local como Ollama pode ter limitações em relação à IA na nuvem  
- Cuidado com limites de token/contexto de cada modelo  
- Validar falhas de autenticação, conexão e parsing ao chamar os provedores

---

### **Context Dump**

Sou desenvolvedor backend sênior e estou construindo uma CLI avançada em Python que funcione como assistente de codificação, com recursos de shell interativo, edição de arquivos, execução de código com IA e planejamento. Preciso de suporte a **múltiplos provedores de IA**, incluindo **Ollama rodando localmente**, com possibilidade de configurar endpoint, modelo e parâmetros em um arquivo local. Quero que o CLI tenha comandos intuitivos, suporte Bash, e capacidade de executar fluxos complexos com sugestões e automações da IA.

---