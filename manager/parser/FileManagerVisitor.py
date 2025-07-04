# Generated from FileManager.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FileManagerParser import FileManagerParser
else:
    from FileManagerParser import FileManagerParser

# This class defines a complete generic visitor for a parse tree produced by FileManagerParser.

class FileManagerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FileManagerParser#programa.
    def visitPrograma(self, ctx:FileManagerParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#declaracaoPastaRaiz.
    def visitDeclaracaoPastaRaiz(self, ctx:FileManagerParser.DeclaracaoPastaRaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#regra.
    def visitRegra(self, ctx:FileManagerParser.RegraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#condicao.
    def visitCondicao(self, ctx:FileManagerParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#expressaoBooleana.
    def visitExpressaoBooleana(self, ctx:FileManagerParser.ExpressaoBooleanaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#variavelMetadata.
    def visitVariavelMetadata(self, ctx:FileManagerParser.VariavelMetadataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#operadorComparacao.
    def visitOperadorComparacao(self, ctx:FileManagerParser.OperadorComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#valor.
    def visitValor(self, ctx:FileManagerParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#acao.
    def visitAcao(self, ctx:FileManagerParser.AcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#moverPara.
    def visitMoverPara(self, ctx:FileManagerParser.MoverParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#copiarPara.
    def visitCopiarPara(self, ctx:FileManagerParser.CopiarParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#renomearPara.
    def visitRenomearPara(self, ctx:FileManagerParser.RenomearParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#excluir.
    def visitExcluir(self, ctx:FileManagerParser.ExcluirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#aplicarTags.
    def visitAplicarTags(self, ctx:FileManagerParser.AplicarTagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#listaTags.
    def visitListaTags(self, ctx:FileManagerParser.ListaTagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FileManagerParser#stringComVariaveis.
    def visitStringComVariaveis(self, ctx:FileManagerParser.StringComVariaveisContext):
        return self.visitChildren(ctx)



del FileManagerParser