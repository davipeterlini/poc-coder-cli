from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def start_shell():
    commands = ['cd', 'ls', 'open', 'edit', 'run', 'ai', 'plan', 'config', 'provider', 'history']
    completer = WordCompleter(commands, ignore_case=True)
    session = PromptSession(completer=completer)

    print("Bem-vindo ao CodeCLI. Digite 'help' para comandos disponíveis.")
    while True:
        try:
            user_input = session.prompt(">>> ")
            if user_input.strip() in ['exit', 'quit']:
                print("Encerrando...")
                break
            # Aqui seria o roteamento para os comandos reais
            print(f"Comando executado: {user_input}")
        except (KeyboardInterrupt, EOFError):
            print("Saindo...")
            break
