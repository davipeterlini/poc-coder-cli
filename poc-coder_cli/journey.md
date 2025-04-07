- 15/03/2025
  - grok
    - Qual a lib para fazer o modo iterativo do Claude Code 
    - Percebi que quando executo o claude code no terminal a parte iterativa é muito boa e intuitiva, existe alguma extensão ou lib que o claude code usa para deixar a estrutura iterativa no terminal da forma como é ? 
    - Como replicar o comportamento se possuo um ferramenta de cli parecida, porém feita em python 
  - coder
    - Crie um arquivo .gitignore e adicione os valores do coder
    - Gere o README para execução dessa aplicação
    - Crie um arquivo .env.local e outro de exemplo para commitar, nele coloque a chave da antrhopic
    - Faça com que a aplicação leia o arquivo .env, se for necessário instalar libs
    - Atualize o readme com os comandos básicos para rodar a aplicação cli
    - Crie o comando de rodar um prompt na API da anthropic e salvar os códigos gerados em arquivos
    - Tudo que está sendo criado pela IA está sendo armazenado a onde, pois não está aparecendo nada na raiz do meu dir
    - Não é só salvar no log é salvar na raiz do projeto os arquivos que forem sendo criados na CLI
    - Coloque os arquivos dentro de uma pasta session/name 
        on name é o nome gerado randomicamente
    - Salve tambem os prompts salvos no arquivo: .cli_history um em cada prompt
    - o comando deve estar em um arquivo e a resposta em outro
      os nomes dos arquivos são 0001_user.md para cada comando vai incrementando o numero 
      e as respostas são 0001_assistants.md para cada comando vai incrementando o numero

      Ou seja, no final de 3 comandos teremos conforme abaixo dentro da sessão criada

      0001_user.md
      0001_assistants.md
      0002_user.md
      0002_assistants.md
      0003_user.md
      0003_assistants.md
    - melhore a estrutura iterativa do terminal para que fique visualmente renderizada e mais bonita
    - Agora preciso realmente executar na raiz da minha aplicação os comandos que a ia gerou
      - Vi que o claude usa libs como BashTool e EditTool é possível usar isso nesse projeto ? 
    - Adicione um scanner de diretórios para fornecer contexto automático
      def scan_project():
        files = []
        for root, _, filenames in os.walk(context["project_dir"]):
            files.extend(os.path.join(root, f) for f in filenames)
        context["files"] = files
        return "\n".join(files)
    - Agora preciso criar uma estrutura de provedor ou seja quero rodar minha aplicação apontando para um modelo local a partir do olhama
      - Construção essa estrutura e classes para suportar isso
    - Ajustes o aruqivo app.py a partir da estrutura da pasta src criada
      - Considere utilizar o clean code e clean arquithecture
      


- 16/03/2025
    - Ao abrir o CLI a função - scan_project deve ser executada
    - Os comandos não estão sendo executados

 