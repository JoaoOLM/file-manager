from antlr4 import CommonTokenStream
from parser.FileManagerLexer import FileManagerLexer
from parser.FileManagerParser import FileManagerParser

def run_syntactic(lexer: FileManagerLexer):
    token_stream = CommonTokenStream(lexer)
    parser = FileManagerParser(token_stream)
    tree = parser.programa()

    return tree