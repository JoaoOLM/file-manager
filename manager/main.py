import os
import sys
from cyclopts import App
from rich.console import Console
from rich.panel import Panel

from manager.bash_gen import generate_bash_script
from manager.lexical import run_lexer
from manager.syntactic import run_syntactic
from manager.semantic import run_semantic

console = Console()
app = App(console=console)

@app.command
def compiler(file_path: str):
    """
    Compilador do gerenciador de arquivos.
    Processa um arquivo de regras (.fm) e gera um script Bash executável.
    """
    console.print("[bold white]Iniciando o compilador de gerenciamento de arquivos...[/bold white]")
    console.print(f"[blue]Analisando o arquivo: [white]{file_path}[/white][/blue]")

    try:
        console.print("[cyan]Fase 1: Análise Léxica[/cyan]")
        lexer = run_lexer(file_path)
        console.print("[green]Análise Léxica concluída.[/green] Tokens gerados.")

        console.print("[cyan]Fase 2: Análise Sintática[/cyan]")
        tree = run_syntactic(lexer)
        console.print("[green]Análise Sintática concluída.[/green] Árvore de sintaxe gerada.")

        console.print("[cyan]Fase 3: Análise Semântica[/cyan]")
        semantic_result = run_semantic(tree)

        if semantic_result["errors"]:
            console.print("[red]Erros Semânticos encontrados:[/red]")
            for error_msg in semantic_result["errors"]:
                console.print(f"  [red]• {error_msg}[/red]")
            console.print("[red]Análise Semântica falhou devido a erros. Não será gerado script.[/red]")
            sys.exit(1) # Sai com código de erro
        
        console.print("[green]Análise Semântica concluída.[/green] Estrutura de regras validada.")

        console.print("[cyan]Fase 4: Geração do Script Bash[/cyan]")
        bash_script = generate_bash_script(semantic_result)
        
        if bash_script:
            output_file = "file_manager_script.sh"
            with open(output_file, "w") as f:
                f.write(bash_script)
            
            os.chmod(output_file, 0o755) 
            
            console.print(
                Panel(
                    f"Script Bash gerado com sucesso!\nCaminho: [bold white]{output_file}[/bold white]\n\n"
                    f"[dim]Para executar, use:[/dim] [green]./{output_file}[/green]",
                    title="[green]COMPILAÇÃO CONCLUÍDA[/green]",
                    border_style="green",
                    padding=(1, 2)
                )
            )
        else:
            console.print("[yellow]Nenhum script Bash gerado (possivelmente nenhuma regra válida).[/yellow]")

    except Exception:
        # Captura qualquer exceção inesperada e imprime o traceback formatado
        console.print("[red]Ocorreu um erro inesperado durante a compilação:[/red]")
        console.print_exception(show_locals=True)
        sys.exit(1)

    sys.exit(0) 