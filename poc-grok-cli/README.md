# Claude Code CLI

Claude Code CLI é uma aplicação de linha de comando (CLI) que replica as funcionalidades do Claude Code, seguindo as melhores práticas de desenvolvimento e segurança. A aplicação é implementada em Python e é compatível com os sistemas operacionais macOS, Ubuntu/Debian e Windows (via WSL). Ela opera diretamente no terminal, entende o contexto do projeto automaticamente sem a necessidade de adicionar arquivos manualmente ao contexto, e suporta comandos em linguagem natural para as seguintes funcionalidades principais:

## Funcionalidades

1. **Edição de Arquivos**: Permitir modificações em arquivos para corrigir bugs ou adicionar novas funcionalidades.
2. **Resolução de Dúvidas**: Responder perguntas sobre a arquitetura do código, lógica ou funcionamento de partes específicas da base de código.
3. **Execução de Comandos**: Executar e corrigir comandos de desenvolvimento, como testes unitários, linting ou outras tarefas relacionadas.
4. **Gerenciamento de Git**: Auxiliar em fluxos de trabalho Git, incluindo pesquisa no histórico de commits, resolução de conflitos de merge, criação de commits e pull requests.

## Requisitos Técnicos

- **Linguagem**: Desenvolvida em Python.
- **Compatibilidade**: Funciona em macOS, Ubuntu/Debian e Windows (via WSL).
- **Integração no Terminal**: Não depende de servidores adicionais, funcionando diretamente no ambiente do terminal.

## Segurança e Permissões

- Implementa um sistema de permissões que solicita aprovação explícita do usuário para operações sensíveis, como alterações em arquivos ou execução de comandos críticos.
- Adota boas práticas de segurança, especialmente em ambientes conteinerizados, para prevenir vulnerabilidades.

## Integração e Experiência do Usuário

- A aplicação se integra ao ambiente de desenvolvimento do usuário e entende o contexto do projeto automaticamente.
- Suporta comandos em linguagem natural para todas as funcionalidades listadas.

## Funcionalidades Adicionais

- Permite a criação de comandos personalizados que podem ser usados em diferentes projetos.
- Oferece integração com o VS Code, especialmente em contêineres de desenvolvimento.

## Exemplos de Uso

- **Edição de Arquivos**: `python main.py edit main.py 42 "print('Hello, World!')"`
- **Resolução de Dúvidas**: `python main.py explain main.py authenticateUser`
- **Execução de Comandos**: `python main.py run "pytest"`
- **Gerenciamento de Git**: `python main.py git commit "Initial commit"`

## Instalação

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd claude-code-cli
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Execute a aplicação com o comando:
```sh
python main.py <comando> <argumentos>
```

## Comandos Disponíveis

- `edit <file> <line> <content>`: Edita um arquivo em uma linha específica com o conteúdo fornecido.
- `explain <file> <function_name>`: Explica como uma função específica funciona no arquivo fornecido.
- `run <command>`: Executa um comando de desenvolvimento.
- `git <action> [options...]`: Executa uma ação do Git.

## Critérios de Sucesso

- A aplicação deve executar todas as funcionalidades listadas com precisão e segurança.
- Deve ser fácil de instalar e configurar, acompanhada de documentação clara e acessível para os usuários.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.