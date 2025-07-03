from antlr4 import FileStream, Token
from parser.FileManagerLexer import FileManagerLexer


def run_lexer(input_file: str):
    """
    Executa a análise léxica do arquivo de entrada e retorna os tokens gerados.
    
    :param input_file: Caminho para o arquivo de entrada.
    :return: Lista de tokens gerados pelo lexer.
    """
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = FileManagerLexer(input_stream)
    
    tokens = []
    for token in lexer.getAllTokens():
        tokens.append((Token.symbolicNames[token.type], token.text))
    
    return lexer