import cmd

class CodeShell(cmd.Cmd):
    intro = "Bem-vindo ao CodeCLI. Digite 'help' para ver os comandos disponíveis."
    prompt = "(code-cli) "

    def do_exit(self, arg):
        "Sair do shell"
        return True

    def do_hello(self, arg):
        "Exemplo de comando"
        print("Olá! Este é um exemplo de comando.")

def interactive_shell():
    CodeShell().cmdloop()
