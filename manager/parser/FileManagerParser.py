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
        4,1,37,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,1,0,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,3,1,
        3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,78,8,8,1,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,97,
        8,14,10,14,12,14,100,9,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,0,4,1,0,5,6,1,0,23,30,1,0,13,22,1,0,31,32,94,0,30,1,
        0,0,0,2,39,1,0,0,0,4,42,1,0,0,0,6,54,1,0,0,0,8,62,1,0,0,0,10,66,
        1,0,0,0,12,68,1,0,0,0,14,70,1,0,0,0,16,77,1,0,0,0,18,79,1,0,0,0,
        20,82,1,0,0,0,22,85,1,0,0,0,24,88,1,0,0,0,26,90,1,0,0,0,28,93,1,
        0,0,0,30,34,3,2,1,0,31,33,3,4,2,0,32,31,1,0,0,0,33,36,1,0,0,0,34,
        32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,0,37,38,5,0,0,
        1,38,1,1,0,0,0,39,40,5,2,0,0,40,41,5,31,0,0,41,3,1,0,0,0,42,43,5,
        3,0,0,43,44,5,4,0,0,44,45,3,6,3,0,45,46,5,7,0,0,46,51,3,16,8,0,47,
        48,5,5,0,0,48,50,3,16,8,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,
        0,0,51,52,1,0,0,0,52,5,1,0,0,0,53,51,1,0,0,0,54,59,3,8,4,0,55,56,
        7,0,0,0,56,58,3,8,4,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,7,1,0,0,0,61,59,1,0,0,0,62,63,3,10,5,0,63,64,3,
        12,6,0,64,65,3,14,7,0,65,9,1,0,0,0,66,67,7,1,0,0,67,11,1,0,0,0,68,
        69,7,2,0,0,69,13,1,0,0,0,70,71,7,3,0,0,71,15,1,0,0,0,72,78,3,18,
        9,0,73,78,3,20,10,0,74,78,3,22,11,0,75,78,3,24,12,0,76,78,3,26,13,
        0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,
        1,0,0,0,78,17,1,0,0,0,79,80,5,8,0,0,80,81,5,31,0,0,81,19,1,0,0,0,
        82,83,5,9,0,0,83,84,5,31,0,0,84,21,1,0,0,0,85,86,5,10,0,0,86,87,
        5,31,0,0,87,23,1,0,0,0,88,89,5,11,0,0,89,25,1,0,0,0,90,91,5,12,0,
        0,91,92,3,28,14,0,92,27,1,0,0,0,93,98,5,31,0,0,94,95,5,1,0,0,95,
        97,5,31,0,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,
        0,0,99,29,1,0,0,0,100,98,1,0,0,0,5,34,51,59,77,98
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
                      "ID", "WS", "COMENTARIO_LINHA", "COMENTARIO_BLOCO" ]

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

    ruleNames =  [ "programa", "declaracaoPastaRaiz", "regra", "condicao", 
                   "expressaoBooleana", "variavelMetadata", "operadorComparacao", 
                   "valor", "acao", "moverPara", "copiarPara", "renomearPara", 
                   "excluir", "aplicarTags", "listaTags" ]

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
            self.state = 30
            self.declaracaoPastaRaiz()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 31
                self.regra()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
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
            self.state = 39
            self.match(FileManagerParser.PASTA_RAIZ)
            self.state = 40
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
            self.state = 42
            self.match(FileManagerParser.REGRA)
            self.state = 43
            self.match(FileManagerParser.SE)
            self.state = 44
            self.condicao()
            self.state = 45
            self.match(FileManagerParser.ENTAO)
            self.state = 46
            self.acao()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 47
                self.match(FileManagerParser.E)
                self.state = 48
                self.acao()
                self.state = 53
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
            self.state = 54
            self.expressaoBooleana()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.expressaoBooleana()
                self.state = 61
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
            self.state = 62
            self.variavelMetadata()
            self.state = 63
            self.operadorComparacao()
            self.state = 64
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
            self.state = 66
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
            self.state = 68
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
            self.state = 70
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.moverPara()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.copiarPara()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.renomearPara()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.excluir()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
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
            self.state = 79
            self.match(FileManagerParser.MOVER_PARA)
            self.state = 80
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
            self.state = 82
            self.match(FileManagerParser.COPIAR_PARA)
            self.state = 83
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

        def STRING(self):
            return self.getToken(FileManagerParser.STRING, 0)

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
            self.state = 85
            self.match(FileManagerParser.RENOMEAR_PARA)
            self.state = 86
            self.match(FileManagerParser.STRING)
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
            self.state = 88
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
            self.state = 90
            self.match(FileManagerParser.APLICAR_TAGS)
            self.state = 91
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
            self.state = 93
            self.match(FileManagerParser.STRING)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 94
                self.match(FileManagerParser.T__0)
                self.state = 95
                self.match(FileManagerParser.STRING)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





