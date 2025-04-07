
**Crie uma aplicação CLI que replique as funcionalidades do Claude Code, seguindo as melhores práticas de desenvolvimento e segurança. A aplicação deve ser implementada em Node.js e ser compatível com os sistemas operacionais macOS, Ubuntu/Debian e Windows (via WSL). Ela deve operar diretamente no terminal, entender o contexto do projeto automaticamente sem a necessidade de adicionar arquivos manualmente ao contexto, e suportar comandos em linguagem natural para as seguintes funcionalidades principais:**

### **Funcionalidades:**
1. **Edição de Arquivos**: Permitir modificações em arquivos para corrigir bugs ou adicionar novas funcionalidades.
2. **Resolução de Dúvidas**: Responder perguntas sobre a arquitetura do código, lógica ou funcionamento de partes específicas da base de código.
3. **Execução de Comandos**: Executar e corrigir comandos de desenvolvimento, como testes unitários, linting ou outras tarefas relacionadas.
4. **Gerenciamento de Git**: Auxiliar em fluxos de trabalho Git, incluindo pesquisa no histórico de commits, resolução de conflitos de merge, criação de commits e pull requests.

### **Requisitos Técnicos:**
- **Linguagem**: Desenvolvida em Node.js.
- **Compatibilidade**: Funcionar em macOS, Ubuntu/Debian e Windows (via WSL).
- **Integração no Terminal**: Não deve depender de servidores adicionais, funcionando diretamente no ambiente do terminal.

### **Segurança e Permissões:**
- Implementar um sistema de permissões que solicite aprovação explícita do usuário para operações sensíveis, como alterações em arquivos ou execução de comandos críticos.
- Adotar boas práticas de segurança, especialmente em ambientes conteinerizados, para prevenir vulnerabilidades.

### **Integração e Experiência do Usuário:**
- A aplicação deve integrar-se ao ambiente de desenvolvimento do usuário e entender o contexto do projeto automaticamente.
- Suportar comandos em linguagem natural para todas as funcionalidades listadas.

### **Funcionalidades Adicionais:**
- Permitir a criação de comandos personalizados que possam ser usados em diferentes projetos.
- Oferecer integração com o VS Code, especialmente em contêineres de desenvolvimento.

### **Exemplos de Uso:**
- **Edição de Arquivos**: "Corrija o bug no arquivo main.js na linha 42."
- **Resolução de Dúvidas**: "Explique como a função authenticateUser funciona."
- **Execução de Comandos**: "Execute os testes unitários e corrija falhas."
- **Gerenciamento de Git**: "Crie um commit com as mudanças atuais e prepare um pull request."

### **Critérios de Sucesso:**
- A aplicação deve executar todas as funcionalidades listadas com precisão e segurança.
- Deve ser fácil de instalar e configurar, acompanhada de documentação clara e acessível para os usuários.