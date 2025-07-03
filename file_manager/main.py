from cyclopts import App
from rich.console import Console
from antlr4 import *
from lexical import run_lexer
from syntactic import run_syntactic

console = Console()
app = App(console=console)


@app.command
def compiler(file_path: str):
    """Compilador do gerenciador de arquivos"""
    try:
        print(f"Analisando o arquivo: {file_path}")
        lexer = run_lexer(file_path)
        print("Análise Léxica concluída. Tokens gerados.")

        print("Iniciando análise Sintática.")
        tree = run_syntactic(lexer)
        print("Análise Sintática concluída. Árvore de sintaxe gerada.")

        print("Iniciando análise Semântica.")
        
        print("Iniciando análise Semântica.")

        return tree
    except ValueError:
        console.print_exception()