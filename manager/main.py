from cyclopts import App
from rich.console import Console
from .lexical import run_lexer
from .syntactic import run_syntactic
from .semantic import SemanticAnalyzer

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
        semantic_analyzer = SemanticAnalyzer()
        semantic_result = semantic_analyzer.visit(tree)
        print("Análise Semântica concluída.")

        if semantic_result["errors"]:
            print("Erros Semânticos encontrados:")
            for error in semantic_result["errors"]:
                console.print(f"[bold red]ERRO:[/bold red] {error}")
            return None # Interrompe a compilação devido a erros

        print("Análise Semântica concluída. Estrutura de regras extraída.")

        return tree
    except ValueError:
        console.print_exception()