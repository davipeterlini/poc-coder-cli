import os
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from rich.console import Console
from anthropic import Anthropic, AnthropicError

# Configuração inicial
console = Console()
client = Anthropic(api_key="sua-chave-api-aqui")  # Substitua pela sua chave
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
        
        except KeyboardInterrupt:
            console.print("[red]Interrompido pelo usuário. Encerrando...[/red]")
            break
        except Exception as e:
            console.print(f"[red]Erro inesperado: {str(e)}[/red]")

if __name__ == "__main__":
    main()