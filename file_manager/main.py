from cyclopts import App
from rich.console import Console
from antlr4 import *
from parser.FileManagerLexer import FileManagerLexer
from parser.FileManagerParser import FileManagerParser

console = Console()
app = App(console=console)


@app.command
def compiler(file_path: str, output_file: str):
    """Compilador do gerenciador de arquivos"""
    try:
        # 1. Carregar o arquivo de entrada
        input_stream = FileStream(file_path, encoding='utf-8')
        print(f"Analisando o arquivo: {file_path}")

        # 2. Análise Léxica (Lexer)
        # Cria o lexer a partir do input stream
        lexer = FileManagerLexer(input_stream)
        # Cria um stream de tokens a partir do lexer
        token_stream = CommonTokenStream(lexer)
        print("Análise Léxica concluída. Tokens gerados.")

        # 3. Análise Sintática (Parser)
        # Cria o parser a partir do stream de tokens
        parser = FileManagerParser(token_stream)
        # Obtém a árvore de sintaxe (parse tree) a partir da regra inicial 'programa'
        tree = parser.programa()
        print("Análise Sintática concluída. Árvore de sintaxe gerada.")

        # Opcional: Imprimir a árvore de sintaxe para depuração
        # print("\nÁrvore de Sintaxe (Parse Tree):")
        # print(tree.toStringTree(recog=parser))

        # Retorna a árvore de sintaxe para a próxima fase (Análise Semântica)
        return tree
    except ValueError:
        console.print_exception()