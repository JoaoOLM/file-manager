from antlr4 import FileStream, Token
from .parser.FileManagerLexer import FileManagerLexer


def run_lexer(input_file: str):
    """
    Executa a análise léxica do arquivo de entrada e retorna o léxico.
    """
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = FileManagerLexer(input_stream)
    
    return lexer