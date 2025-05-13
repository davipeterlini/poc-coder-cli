import typer
from code_cli.cli.interactive_shell import start_shell

app = typer.Typer()

@app.command()
def shell():
    """Inicia a CLI interativa com suporte a IA"""
    start_shell()

if __name__ == "__main__":
    app()
