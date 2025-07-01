# Generated from FileManager.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,12,2,55,
        9,2,1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,80,8,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,
        14,5,14,99,8,14,10,14,12,14,102,9,14,1,15,4,15,105,8,15,11,15,12,
        15,106,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,
        5,1,0,5,6,1,0,23,30,1,0,13,22,1,0,31,32,1,0,38,39,101,0,32,1,0,0,
        0,2,41,1,0,0,0,4,44,1,0,0,0,6,56,1,0,0,0,8,64,1,0,0,0,10,68,1,0,
        0,0,12,70,1,0,0,0,14,72,1,0,0,0,16,79,1,0,0,0,18,81,1,0,0,0,20,84,
        1,0,0,0,22,87,1,0,0,0,24,90,1,0,0,0,26,92,1,0,0,0,28,95,1,0,0,0,
        30,104,1,0,0,0,32,36,3,2,1,0,33,35,3,4,2,0,34,33,1,0,0,0,35,38,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,
        40,5,0,0,1,40,1,1,0,0,0,41,42,5,2,0,0,42,43,5,31,0,0,43,3,1,0,0,
        0,44,45,5,3,0,0,45,46,5,4,0,0,46,47,3,6,3,0,47,48,5,7,0,0,48,53,
        3,16,8,0,49,50,5,5,0,0,50,52,3,16,8,0,51,49,1,0,0,0,52,55,1,0,0,
        0,53,51,1,0,0,0,53,54,1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,0,56,61,3,
        8,4,0,57,58,7,0,0,0,58,60,3,8,4,0,59,57,1,0,0,0,60,63,1,0,0,0,61,
        59,1,0,0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,61,1,0,0,0,64,65,3,10,5,
        0,65,66,3,12,6,0,66,67,3,14,7,0,67,9,1,0,0,0,68,69,7,1,0,0,69,11,
        1,0,0,0,70,71,7,2,0,0,71,13,1,0,0,0,72,73,7,3,0,0,73,15,1,0,0,0,
        74,80,3,18,9,0,75,80,3,20,10,0,76,80,3,22,11,0,77,80,3,24,12,0,78,
        80,3,26,13,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,
        0,0,79,78,1,0,0,0,80,17,1,0,0,0,81,82,5,8,0,0,82,83,5,31,0,0,83,
        19,1,0,0,0,84,85,5,9,0,0,85,86,5,31,0,0,86,21,1,0,0,0,87,88,5,10,
        0,0,88,89,3,30,15,0,89,23,1,0,0,0,90,91,5,11,0,0,91,25,1,0,0,0,92,
        93,5,12,0,0,93,94,3,28,14,0,94,27,1,0,0,0,95,100,5,31,0,0,96,97,
        5,1,0,0,97,99,5,31,0,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,
        0,100,101,1,0,0,0,101,29,1,0,0,0,102,100,1,0,0,0,103,105,7,4,0,0,
        104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,
        107,31,1,0,0,0,6,36,53,61,79,100,106
    ]

class FileManagerParser ( Parser ):

    grammarFileName = "FileManager.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'PASTA_RAIZ'", "'REGRA'", "'SE'", 
                     "'E'", "'OU'", "'ENTAO'", "'MOVER_PARA'", "'COPIAR_PARA'", 
                     "'RENOMEAR_PARA'", "'EXCLUIR'", "'APLICAR_TAGS'", "'EH'", 
                     "'NAO_EH'", "'CONTEM'", "'NAO_CONTEM'", "'COMECA_COM'", 
                     "'TERMINA_COM'", "'MAIOR_QUE'", "'MENOR_QUE'", "'IGUAL_OU_MAIOR_QUE'", 
                     "'IGUAL_OU_MENOR_QUE'", "'$NOME'", "'$NOME_BASE'", 
                     "'$EXTENSAO'", "'$TAMANHO_KB'", "'$TAMANHO_MB'", "'$DATA_CRIACAO'", 
                     "'$DATA_MODIFICACAO'", "'$TIPO_MIME'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PASTA_RAIZ", "REGRA", "SE", 
                      "E", "OU", "ENTAO", "MOVER_PARA", "COPIAR_PARA", "RENOMEAR_PARA", 
                      "EXCLUIR", "APLICAR_TAGS", "EH", "NAO_EH", "CONTEM", 
                      "NAO_CONTEM", "COMECA_COM", "TERMINA_COM", "MAIOR_QUE", 
                      "MENOR_QUE", "IGUAL_OU_MAIOR_QUE", "IGUAL_OU_MENOR_QUE", 
                      "VAR_NOME", "VAR_NOME_BASE", "VAR_EXTENSAO", "VAR_TAMANHO_KB", 
                      "VAR_TAMANHO_MB", "VAR_DATA_CRIACAO", "VAR_DATA_MODIFICACAO", 
                      "VAR_TIPO_MIME", "STRING", "NUMERO", "DIRETORIO", 
                      "ID", "WS", "COMENTARIO_LINHA", "COMENTARIO_BLOCO", 
                      "STRING_PARTE", "VARIAVEL_INTERPOLADA" ]

    RULE_programa = 0
    RULE_declaracaoPastaRaiz = 1
    RULE_regra = 2
    RULE_condicao = 3
    RULE_expressaoBooleana = 4
    RULE_variavelMetadata = 5
    RULE_operadorComparacao = 6
    RULE_valor = 7
    RULE_acao = 8
    RULE_moverPara = 9
    RULE_copiarPara = 10
    RULE_renomearPara = 11
    RULE_excluir = 12
    RULE_aplicarTags = 13
    RULE_listaTags = 14
    RULE_stringComVariaveis = 15

    ruleNames =  [ "programa", "declaracaoPastaRaiz", "regra", "condicao", 
                   "expressaoBooleana", "variavelMetadata", "operadorComparacao", 
                   "valor", "acao", "moverPara", "copiarPara", "renomearPara", 
                   "excluir", "aplicarTags", "listaTags", "stringComVariaveis" ]

    EOF = Token.EOF
    T__0=1
    PASTA_RAIZ=2
    REGRA=3
    SE=4
    E=5
    OU=6
    ENTAO=7
    MOVER_PARA=8
    COPIAR_PARA=9
    RENOMEAR_PARA=10
    EXCLUIR=11
    APLICAR_TAGS=12
    EH=13
    NAO_EH=14
    CONTEM=15
    NAO_CONTEM=16
    COMECA_COM=17
    TERMINA_COM=18
    MAIOR_QUE=19
    MENOR_QUE=20
    IGUAL_OU_MAIOR_QUE=21
    IGUAL_OU_MENOR_QUE=22
    VAR_NOME=23
    VAR_NOME_BASE=24
    VAR_EXTENSAO=25
    VAR_TAMANHO_KB=26
    VAR_TAMANHO_MB=27
    VAR_DATA_CRIACAO=28
    VAR_DATA_MODIFICACAO=29
    VAR_TIPO_MIME=30
    STRING=31
    NUMERO=32
    DIRETORIO=33
    ID=34
    WS=35
    COMENTARIO_LINHA=36
    COMENTARIO_BLOCO=37
    STRING_PARTE=38
    VARIAVEL_INTERPOLADA=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoPastaRaiz(self):
            return self.getTypedRuleContext(FileManagerParser.DeclaracaoPastaRaizContext,0)


        def EOF(self):
            return self.getToken(FileManagerParser.EOF, 0)

        def regra(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FileManagerParser.RegraContext)
            else:
                return self.getTypedRuleContext(FileManagerParser.RegraContext,i)


        def getRuleIndex(self):
            return FileManagerParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = FileManagerParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.declaracaoPastaRaiz()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 33
                self.regra()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(FileManagerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoPastaRaizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASTA_RAIZ(self):
            return self.getToken(FileManagerParser.PASTA_RAIZ, 0)

        def STRING(self):
            return self.getToken(FileManagerParser.STRING, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_declaracaoPastaRaiz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoPastaRaiz" ):
                listener.enterDeclaracaoPastaRaiz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoPastaRaiz" ):
                listener.exitDeclaracaoPastaRaiz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoPastaRaiz" ):
                return visitor.visitDeclaracaoPastaRaiz(self)
            else:
                return visitor.visitChildren(self)




    def declaracaoPastaRaiz(self):

        localctx = FileManagerParser.DeclaracaoPastaRaizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracaoPastaRaiz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(FileManagerParser.PASTA_RAIZ)
            self.state = 42
            self.match(FileManagerParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGRA(self):
            return self.getToken(FileManagerParser.REGRA, 0)

        def SE(self):
            return self.getToken(FileManagerParser.SE, 0)

        def condicao(self):
            return self.getTypedRuleContext(FileManagerParser.CondicaoContext,0)


        def ENTAO(self):
            return self.getToken(FileManagerParser.ENTAO, 0)

        def acao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FileManagerParser.AcaoContext)
            else:
                return self.getTypedRuleContext(FileManagerParser.AcaoContext,i)


        def E(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.E)
            else:
                return self.getToken(FileManagerParser.E, i)

        def getRuleIndex(self):
            return FileManagerParser.RULE_regra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegra" ):
                listener.enterRegra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegra" ):
                listener.exitRegra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegra" ):
                return visitor.visitRegra(self)
            else:
                return visitor.visitChildren(self)




    def regra(self):

        localctx = FileManagerParser.RegraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_regra)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(FileManagerParser.REGRA)
            self.state = 45
            self.match(FileManagerParser.SE)
            self.state = 46
            self.condicao()
            self.state = 47
            self.match(FileManagerParser.ENTAO)
            self.state = 48
            self.acao()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 49
                self.match(FileManagerParser.E)
                self.state = 50
                self.acao()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoBooleana(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FileManagerParser.ExpressaoBooleanaContext)
            else:
                return self.getTypedRuleContext(FileManagerParser.ExpressaoBooleanaContext,i)


        def E(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.E)
            else:
                return self.getToken(FileManagerParser.E, i)

        def OU(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.OU)
            else:
                return self.getToken(FileManagerParser.OU, i)

        def getRuleIndex(self):
            return FileManagerParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)




    def condicao(self):

        localctx = FileManagerParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.expressaoBooleana()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 57
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                self.expressaoBooleana()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavelMetadata(self):
            return self.getTypedRuleContext(FileManagerParser.VariavelMetadataContext,0)


        def operadorComparacao(self):
            return self.getTypedRuleContext(FileManagerParser.OperadorComparacaoContext,0)


        def valor(self):
            return self.getTypedRuleContext(FileManagerParser.ValorContext,0)


        def getRuleIndex(self):
            return FileManagerParser.RULE_expressaoBooleana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoBooleana" ):
                listener.enterExpressaoBooleana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoBooleana" ):
                listener.exitExpressaoBooleana(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoBooleana" ):
                return visitor.visitExpressaoBooleana(self)
            else:
                return visitor.visitChildren(self)




    def expressaoBooleana(self):

        localctx = FileManagerParser.ExpressaoBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressaoBooleana)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.variavelMetadata()
            self.state = 65
            self.operadorComparacao()
            self.state = 66
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariavelMetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NOME(self):
            return self.getToken(FileManagerParser.VAR_NOME, 0)

        def VAR_NOME_BASE(self):
            return self.getToken(FileManagerParser.VAR_NOME_BASE, 0)

        def VAR_EXTENSAO(self):
            return self.getToken(FileManagerParser.VAR_EXTENSAO, 0)

        def VAR_TAMANHO_KB(self):
            return self.getToken(FileManagerParser.VAR_TAMANHO_KB, 0)

        def VAR_TAMANHO_MB(self):
            return self.getToken(FileManagerParser.VAR_TAMANHO_MB, 0)

        def VAR_DATA_CRIACAO(self):
            return self.getToken(FileManagerParser.VAR_DATA_CRIACAO, 0)

        def VAR_DATA_MODIFICACAO(self):
            return self.getToken(FileManagerParser.VAR_DATA_MODIFICACAO, 0)

        def VAR_TIPO_MIME(self):
            return self.getToken(FileManagerParser.VAR_TIPO_MIME, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_variavelMetadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavelMetadata" ):
                listener.enterVariavelMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavelMetadata" ):
                listener.exitVariavelMetadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariavelMetadata" ):
                return visitor.visitVariavelMetadata(self)
            else:
                return visitor.visitChildren(self)




    def variavelMetadata(self):

        localctx = FileManagerParser.VariavelMetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variavelMetadata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2139095040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EH(self):
            return self.getToken(FileManagerParser.EH, 0)

        def NAO_EH(self):
            return self.getToken(FileManagerParser.NAO_EH, 0)

        def CONTEM(self):
            return self.getToken(FileManagerParser.CONTEM, 0)

        def NAO_CONTEM(self):
            return self.getToken(FileManagerParser.NAO_CONTEM, 0)

        def COMECA_COM(self):
            return self.getToken(FileManagerParser.COMECA_COM, 0)

        def TERMINA_COM(self):
            return self.getToken(FileManagerParser.TERMINA_COM, 0)

        def MAIOR_QUE(self):
            return self.getToken(FileManagerParser.MAIOR_QUE, 0)

        def MENOR_QUE(self):
            return self.getToken(FileManagerParser.MENOR_QUE, 0)

        def IGUAL_OU_MAIOR_QUE(self):
            return self.getToken(FileManagerParser.IGUAL_OU_MAIOR_QUE, 0)

        def IGUAL_OU_MENOR_QUE(self):
            return self.getToken(FileManagerParser.IGUAL_OU_MENOR_QUE, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_operadorComparacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorComparacao" ):
                listener.enterOperadorComparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorComparacao" ):
                listener.exitOperadorComparacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorComparacao" ):
                return visitor.visitOperadorComparacao(self)
            else:
                return visitor.visitChildren(self)




    def operadorComparacao(self):

        localctx = FileManagerParser.OperadorComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operadorComparacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8380416) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FileManagerParser.STRING, 0)

        def NUMERO(self):
            return self.getToken(FileManagerParser.NUMERO, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = FileManagerParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moverPara(self):
            return self.getTypedRuleContext(FileManagerParser.MoverParaContext,0)


        def copiarPara(self):
            return self.getTypedRuleContext(FileManagerParser.CopiarParaContext,0)


        def renomearPara(self):
            return self.getTypedRuleContext(FileManagerParser.RenomearParaContext,0)


        def excluir(self):
            return self.getTypedRuleContext(FileManagerParser.ExcluirContext,0)


        def aplicarTags(self):
            return self.getTypedRuleContext(FileManagerParser.AplicarTagsContext,0)


        def getRuleIndex(self):
            return FileManagerParser.RULE_acao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcao" ):
                listener.enterAcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcao" ):
                listener.exitAcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcao" ):
                return visitor.visitAcao(self)
            else:
                return visitor.visitChildren(self)




    def acao(self):

        localctx = FileManagerParser.AcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_acao)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.moverPara()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.copiarPara()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.renomearPara()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.excluir()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.aplicarTags()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoverParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVER_PARA(self):
            return self.getToken(FileManagerParser.MOVER_PARA, 0)

        def STRING(self):
            return self.getToken(FileManagerParser.STRING, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_moverPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoverPara" ):
                listener.enterMoverPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoverPara" ):
                listener.exitMoverPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoverPara" ):
                return visitor.visitMoverPara(self)
            else:
                return visitor.visitChildren(self)




    def moverPara(self):

        localctx = FileManagerParser.MoverParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_moverPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(FileManagerParser.MOVER_PARA)
            self.state = 82
            self.match(FileManagerParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CopiarParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COPIAR_PARA(self):
            return self.getToken(FileManagerParser.COPIAR_PARA, 0)

        def STRING(self):
            return self.getToken(FileManagerParser.STRING, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_copiarPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCopiarPara" ):
                listener.enterCopiarPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCopiarPara" ):
                listener.exitCopiarPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCopiarPara" ):
                return visitor.visitCopiarPara(self)
            else:
                return visitor.visitChildren(self)




    def copiarPara(self):

        localctx = FileManagerParser.CopiarParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_copiarPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(FileManagerParser.COPIAR_PARA)
            self.state = 85
            self.match(FileManagerParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenomearParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RENOMEAR_PARA(self):
            return self.getToken(FileManagerParser.RENOMEAR_PARA, 0)

        def stringComVariaveis(self):
            return self.getTypedRuleContext(FileManagerParser.StringComVariaveisContext,0)


        def getRuleIndex(self):
            return FileManagerParser.RULE_renomearPara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRenomearPara" ):
                listener.enterRenomearPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRenomearPara" ):
                listener.exitRenomearPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRenomearPara" ):
                return visitor.visitRenomearPara(self)
            else:
                return visitor.visitChildren(self)




    def renomearPara(self):

        localctx = FileManagerParser.RenomearParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_renomearPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(FileManagerParser.RENOMEAR_PARA)
            self.state = 88
            self.stringComVariaveis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExcluirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLUIR(self):
            return self.getToken(FileManagerParser.EXCLUIR, 0)

        def getRuleIndex(self):
            return FileManagerParser.RULE_excluir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcluir" ):
                listener.enterExcluir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcluir" ):
                listener.exitExcluir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExcluir" ):
                return visitor.visitExcluir(self)
            else:
                return visitor.visitChildren(self)




    def excluir(self):

        localctx = FileManagerParser.ExcluirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_excluir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(FileManagerParser.EXCLUIR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AplicarTagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APLICAR_TAGS(self):
            return self.getToken(FileManagerParser.APLICAR_TAGS, 0)

        def listaTags(self):
            return self.getTypedRuleContext(FileManagerParser.ListaTagsContext,0)


        def getRuleIndex(self):
            return FileManagerParser.RULE_aplicarTags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAplicarTags" ):
                listener.enterAplicarTags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAplicarTags" ):
                listener.exitAplicarTags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicarTags" ):
                return visitor.visitAplicarTags(self)
            else:
                return visitor.visitChildren(self)




    def aplicarTags(self):

        localctx = FileManagerParser.AplicarTagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_aplicarTags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(FileManagerParser.APLICAR_TAGS)
            self.state = 93
            self.listaTags()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaTagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.STRING)
            else:
                return self.getToken(FileManagerParser.STRING, i)

        def getRuleIndex(self):
            return FileManagerParser.RULE_listaTags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaTags" ):
                listener.enterListaTags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaTags" ):
                listener.exitListaTags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaTags" ):
                return visitor.visitListaTags(self)
            else:
                return visitor.visitChildren(self)




    def listaTags(self):

        localctx = FileManagerParser.ListaTagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listaTags)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(FileManagerParser.STRING)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 96
                self.match(FileManagerParser.T__0)
                self.state = 97
                self.match(FileManagerParser.STRING)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringComVariaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_PARTE(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.STRING_PARTE)
            else:
                return self.getToken(FileManagerParser.STRING_PARTE, i)

        def VARIAVEL_INTERPOLADA(self, i:int=None):
            if i is None:
                return self.getTokens(FileManagerParser.VARIAVEL_INTERPOLADA)
            else:
                return self.getToken(FileManagerParser.VARIAVEL_INTERPOLADA, i)

        def getRuleIndex(self):
            return FileManagerParser.RULE_stringComVariaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringComVariaveis" ):
                listener.enterStringComVariaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringComVariaveis" ):
                listener.exitStringComVariaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringComVariaveis" ):
                return visitor.visitStringComVariaveis(self)
            else:
                return visitor.visitChildren(self)




    def stringComVariaveis(self):

        localctx = FileManagerParser.StringComVariaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stringComVariaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==38 or _la==39):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38 or _la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





