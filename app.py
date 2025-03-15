import os
import sys
import random
import string
import subprocess
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.local
load_dotenv('.env.local')

# Configuração inicial
console = Console()
session = PromptSession(history=FileHistory(".cli_history"), multiline=False)
context = {"project_dir": os.getcwd(), "previous_commands": [], "files": []}  # Contexto persistente

# Gerar um nome de sessão aleatório
session_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
session_dir = os.path.join("session", session_name)
os.makedirs(session_dir, exist_ok=True)

# Estilo para o prompt
style = Style.from_dict({
    'prompt': 'bold cyan',
    'response': 'bold green',
    'error': 'bold red',
    'info': 'bold yellow'
})

def scan_project():
    """Escaneia o diretório do projeto e atualiza o contexto com a lista de arquivos."""
    files = []
    for root, _, filenames in os.walk(context["project_dir"]):
        files.extend(os.path.join(root, f) for f in filenames)
    context["files"] = files
    return "\n".join(files)

class ModelProvider:
    """Classe base para provedores de modelos."""
    def process_command(self, command, context):
        raise NotImplementedError("Subclasses devem implementar este método")

class AnthropicProvider(ModelProvider):
    """Provedor de modelo para a API do Anthropic."""
    def __init__(self, api_key):
        from anthropic import Anthropic, AnthropicError
        self.client = Anthropic(api_key=api_key)
        self.AnthropicError = AnthropicError

    def process_command(self, command, context):
        try:
            # Adiciona o comando ao contexto
            context["previous_commands"].append(command)
            
            # Escaneia o projeto para obter a lista de arquivos
            project_files = scan_project()
            
            # Monta o prompt com contexto
            prompt = f"Diretório atual: {context['project_dir']}\nArquivos do projeto:\n{project_files}\nComandos anteriores: {context['previous_commands'][-3:]}\nComando atual: {command}"
            
            # Chama a API do Claude
            response = self.client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text  # Ajuste conforme a estrutura da resposta
        except self.AnthropicError as e:
            return f"Erro ao processar o comando: {str(e)}"

class OlhamaProvider(ModelProvider):
    """Provedor de modelo para um modelo local a partir do Olhama."""
    def process_command(self, command, context):
        # Implementação fictícia para o modelo local
        # Aqui você deve adicionar a lógica para processar o comando usando o modelo local do Olhama
        return f"Resposta do modelo local para o comando: {command}"

def execute_shell_command(command):
    """Executa um comando de shell na raiz do projeto."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=context["project_dir"])
        return result.stdout + result.stderr
    except Exception as e:
        return f"Erro ao executar o comando: {str(e)}"

def apply_action(command, response):
    """Aplica ações no sistema de arquivos com base na resposta da IA."""
    console.print(Panel(Text(response, style="response"), title="Resposta da IA", subtitle="Processado"))
    if "editar arquivo" in response.lower():
        # Exemplo simplificado: editar um arquivo
        file_path = Prompt.ask("Qual arquivo deseja editar?", console=console)
        with open(file_path, "a") as f:
            f.write("\n# Editado pela CLI\n")
        console.print(f"[green]Arquivo {file_path} editado![/green]")
    elif "salvar código" in response.lower():
        # Salvar código gerado em um arquivo
        file_path = Prompt.ask("Digite o caminho do arquivo para salvar o código", console=console)
        with open(file_path, "w") as f:
            f.write(response)
        console.print(f"[green]Código salvo em {file_path}![/green]")
    elif "executar comando" in response.lower():
        # Executar um comando de shell
        shell_command = Prompt.ask("Digite o comando de shell para executar", console=console)
        shell_output = execute_shell_command(shell_command)
        console.print(Panel(Text(shell_output, style="info"), title="Saída do Comando", subtitle="Executado"))
    else:
        # Salvar o comando e a resposta em arquivos na pasta da sessão
        file_index = len(context["previous_commands"])
        user_file_name = f"{file_index:04d}_user.md"
        assistant_file_name = f"{file_index:04d}_assistant.md"
        
        user_file_path = os.path.join(session_dir, user_file_name)
        assistant_file_path = os.path.join(session_dir, assistant_file_name)
        
        with open(user_file_path, "w") as user_file:
            user_file.write(command)
        
        with open(assistant_file_path, "w") as assistant_file:
            assistant_file.write(response)
        
        console.print(f"[green]Comando salvo em {user_file_path} e resposta salva em {assistant_file_path}![/green]")

def main():
    # Seleciona o provedor de modelo com base em uma variável de ambiente
    provider_type = os.getenv("MODEL_PROVIDER", "anthropic")
    if provider_type == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        provider = AnthropicProvider(api_key)
    elif provider_type == "olhama":
        provider = OlhamaProvider()
    else:
        console.print("[red]Erro: Provedor de modelo desconhecido.[/red]")
        sys.exit(1)

    console.print(Panel(Text(f"CLI Iterativa - Sessão: {session_name} - Digite 'sair' para encerrar", style="prompt"), title="Bem-vindo", subtitle="Início"))
    
    while True:
        try:
            # Captura o comando do usuário
            command = session.prompt(">> ", style=style)
            if command.lower() == "sair":
                console.print(Panel(Text("Encerrando...", style="error"), title="Saindo", subtitle="Fim"))
                break
            
            # Processa o comando
            console.print(Panel(Text("Processando...", style="info"), title="Aguarde", subtitle="Processamento"))
            response = provider.process_command(command, context)
            
            # Exibe e aplica a resposta
            apply_action(command, response)
        
        except KeyboardInterrupt:
            console.print(Panel(Text("Interrompido pelo usuário. Encerrando...", style="error"), title="Interrompido", subtitle="Fim"))
            break
        except Exception as e:
            console.print(Panel(Text(f"Erro inesperado: {str(e)}", style="error"), title="Erro", subtitle="Exceção"))

if __name__ == "__main__":
    main()