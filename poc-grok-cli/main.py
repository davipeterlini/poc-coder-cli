import click
import os
import subprocess
from git import Repo

@click.group()
def cli():
    pass

@cli.command()
@click.argument('file')
@click.argument('line', type=int)
@click.argument('content')
def edit(file, line, content):
    """Edit a file at a specific line with the provided content"""
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        lines[line - 1] = content + '\n'
        with open(file, 'w') as f:
            f.writelines(lines)
        click.echo(f'File {file} edited successfully at line {line}')
    except Exception as e:
        click.echo(f'Error editing file: {e}')

@cli.command()
@click.argument('file')
@click.argument('function_name')
def explain(file, function_name):
    """Explain how a specific function works in the given file"""
    try:
        with open(file, 'r') as f:
            data = f.read()
        import re
        pattern = rf'def {function_name}\s*\(([^)]*)\)\s*:\s*([^#]*)'
        match = re.search(pattern, data)
        if match:
            click.echo(f'Function {function_name} found:\n{match.group(0)}')
        else:
            click.echo(f'Function {function_name} not found in file {file}')
    except Exception as e:
        click.echo(f'Error explaining function: {e}')

@cli.command()
@click.argument('command')
def run(command):
    """Run a development command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        click.echo(result.stdout)
        if result.stderr:
            click.echo(result.stderr, err=True)
    except Exception as e:
        click.echo(f'Error running command: {e}')

@cli.command()
@click.argument('action')
@click.argument('options', nargs=-1)
def git(action, options):
    """Perform a git action"""
    try:
        repo = Repo(os.getcwd())
        if action == 'commit':
            repo.git.commit('-m', options[0])
            click.echo('Commit successful')
        elif action == 'pull':
            repo.remotes.origin.pull()
            click.echo('Pull successful')
        elif action == 'push':
            repo.remotes.origin.push()
            click.echo('Push successful')
        else:
            click.echo(f'Unknown git action: {action}')
    except Exception as e:
        click.echo(f'Error performing git action: {e}')

if __name__ == '__main__':
    cli()