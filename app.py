import os
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from rich.console import Console
from anthropic import Anthropic, AnthropicError
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env.local
load_dotenv('.env.local')

# Configuração inicial
console = Console()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    console.print("[red]Erro: Chave da API do Anthropic não encontrada. Verifique o arquivo .env.local[/red]")
    sys.exit(1)

client = Anthropic(api_key=api_key)
session = PromptSession(history=FileHistory(".cli_history"), multiline=False)
context = {"project_dir": os.getcwd(), "previous_commands": []}  # Contexto persistente

def process_command(command):
    """Processa o comando do usuário e retorna a resposta da IA."""
    try:
        # Adiciona o comando ao contexto
        context["previous_commands"].append(command)
        
        # Monta o prompt com contexto
        prompt = f"Diretório atual: {context['project_dir']}\nComandos anteriores: {context['previous_commands'][-3:]}\nComando atual: {command}"
        
        # Chama a API do Claude
        response = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text  # Ajuste conforme a estrutura da resposta
    except AnthropicError as e:
        return f"Erro ao processar o comando: {str(e)}"

def apply_action(response):
    """Aplica ações no sistema de arquivos com base na resposta da IA."""
    console.print(f"[yellow]Resposta da IA:[/yellow] {response}")
    if "editar arquivo" in response.lower():
        # Exemplo simplificado: editar um arquivo
        file_path = input("Qual arquivo deseja editar? ")
        with open(file_path, "a") as f:
            f.write("\n# Editado pela CLI\n")
        console.print(f"[green]Arquivo {file_path} editado![/green]")
    elif "salvar código" in response.lower():
        # Salvar código gerado em um arquivo
        file_path = input("Digite o caminho do arquivo para salvar o código: ")
        with open(file_path, "w") as f:
            f.write(response)
        console.print(f"[green]Código salvo em {file_path}![/green]")

def log_response(command, response):
    """Salva o comando e a resposta da IA em um arquivo de log."""
    with open("ia_responses.log", "a") as log_file:
        log_file.write(f"Comando: {command}\nResposta: {response}\n\n")

def main():
    console.print("[bold cyan]CLI Iterativa - Digite 'sair' para encerrar[/bold cyan]")
    
    while True:
        try:
            # Captura o comando do usuário
            command = session.prompt(">> ")
            if command.lower() == "sair":
                console.print("[red]Encerrando...[/red]")
                break
            
            # Processa o comando
            console.print("[italic]Processando...[/italic]")
            response = process_command(command)
            
            # Exibe e aplica a resposta
            apply_action(response)
            
            # Salva a resposta no log
            log_response(command, response)
        
        except KeyboardInterrupt:
            console.print("[red]Interrompido pelo usuário. Encerrando...[/red]")
            break
        except Exception as e:
            console.print(f"[red]Erro inesperado: {str(e)}[/red]")

if __name__ == "__main__":
    main()