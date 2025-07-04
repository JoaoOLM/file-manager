from .parser.FileManagerParser import FileManagerParser
from .parser.FileManagerVisitor import FileManagerVisitor


class SemanticAnalyzer(FileManagerVisitor):
    def __init__(self):
        super().__init__()
        self.root_directory = None
        self.rules = []
        self.errors = []  # Para coletar erros semânticos

        # Dicionário para mapear operadores de comparação para tipos esperados
        # Isso é útil para a verificação de tipos.
        self.type_map = {
            # String comparisons
            FileManagerParser.EH: ['STRING'],
            FileManagerParser.NAO_EH: ['STRING'],
            FileManagerParser.CONTEM: ['STRING'],
            FileManagerParser.NAO_CONTEM: ['STRING'],
            FileManagerParser.COMECA_COM: ['STRING'],
            FileManagerParser.TERMINA_COM: ['STRING'],
            # Numeric comparisons
            FileManagerParser.MAIOR_QUE: ['NUMERO'],
            FileManagerParser.MENOR_QUE: ['NUMERO'],
            FileManagerParser.IGUAL_OU_MAIOR_QUE: ['NUMERO'],
            FileManagerParser.IGUAL_OU_MENOR_QUE: ['NUMERO'],
            # Mixed types (for cases where both might apply, or specific vars)
            # Note: $NOME, $NOME_BASE, $EXTENSAO, $TIPO_MIME will always be STRING
            # $TAMANHO_KB, $TAMANHO_MB will always be NUMERO
            # $DATA_CRIACAO, $DATA_MODIFICACAO are complex, for now treat as STRING for direct comparison,
            # but in a real scenario, you'd need date parsing.
        }

        # Dicionário para mapear variáveis de metadados para seus tipos esperados
        self.variable_types = {
            FileManagerParser.VAR_NOME: 'STRING',
            FileManagerParser.VAR_NOME_BASE: 'STRING',
            FileManagerParser.VAR_EXTENSAO: 'STRING',
            FileManagerParser.VAR_TAMANHO_KB: 'NUMERO',
            FileManagerParser.VAR_TAMANHO_MB: 'NUMERO',
            FileManagerParser.VAR_DATA_CRIACAO: 'STRING',  # Simplificado, idealmente um tipo Data
            FileManagerParser.VAR_DATA_MODIFICACAO: 'STRING',  # Simplificado, idealmente um tipo Data
            FileManagerParser.VAR_TIPO_MIME: 'STRING',
        }

    def visitPrograma(self, ctx: FileManagerParser.ProgramaContext):
        # A primeira coisa que visitamos é a declaração da pasta raiz
        self.visit(ctx.declaracaoPastaRaiz())
        # Depois, visitamos todas as regras
        for regra_ctx in ctx.regra():
            self.visit(regra_ctx)

        # Após a visita completa, você pode retornar a estrutura coletada
        return {
            'root_directory': self.root_directory,
            'rules': self.rules,
            'errors': self.errors,
        }

    def visitDeclaracaoPastaRaiz(
        self, ctx: FileManagerParser.DeclaracaoPastaRaizContext
    ):
        # Extrai o caminho da pasta raiz e remove as aspas
        self.root_directory = ctx.STRING().getText().strip('"')

    def visitRegra(self, ctx: FileManagerParser.RegraContext):
        current_rule = {'conditions': [], 'actions': []}

        # Visita a condição
        condition_result = self.visit(ctx.condicao())
        if condition_result:
            current_rule['conditions'] = condition_result

        # Visita as ações
        for acao_ctx in ctx.acao():
            action_result = self.visit(acao_ctx)
            if action_result:
                current_rule['actions'].append(action_result)

        self.rules.append(current_rule)

    def visitCondicao(self, ctx: FileManagerParser.CondicaoContext):
        conditions = []
        for i, expr_ctx in enumerate(ctx.expressaoBooleana()):
            expr = self.visit(expr_ctx)
            if expr:
                conditions.append(expr)
                # Adiciona o operador lógico (E/OU) se houver mais de uma expressão
                if i < len(ctx.expressaoBooleana()) - 1:
                    op = ctx.getChild(2 * i + 1).getText()  # Pega o token E ou OU
                    conditions.append(op)
        return conditions

    def visitExpressaoBooleana(self, ctx: FileManagerParser.ExpressaoBooleanaContext):
        var_metadata_token = ctx.variavelMetadata().children[0].symbol
        op_comparacao_token = ctx.operadorComparacao().children[0].symbol
        valor_ctx = ctx.valor()

        var_name = var_metadata_token.text
        operator_name = op_comparacao_token.text

        expected_type = self.variable_types.get(var_metadata_token.type)
        if not expected_type:
            self.errors.append(
                f'Erro semântico: Variável de metadado desconhecida: {var_name}'
            )
            return None

        # Verifica o tipo do valor literal
        if valor_ctx.STRING():
            actual_type = 'STRING'
            value = valor_ctx.STRING().getText().strip('"')
        elif valor_ctx.NUMERO():
            actual_type = 'NUMERO'
            value = valor_ctx.NUMERO().getText()
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                self.errors.append(f'Erro semântico: Valor numérico inválido: {value}')
                return None
        else:
            self.errors.append(
                'Erro semântico: Tipo de valor inesperado na expressão booleana.'
            )
            return None

        # **Verificação de Tipo Semântica:**
        # Verifica se o operador de comparação é compatível com o tipo da variável de metadado
        compatible_types = self.type_map.get(op_comparacao_token.type)
        if compatible_types and actual_type not in compatible_types:
            # Exceções para $DATA_CRIACAO e $DATA_MODIFICACAO com operadores de número
            # Se você tratar DATA como STRING por enquanto, isso não será um problema aqui.
            # Mas se você quiser verificar datas como números (maior/menor), precisaria de um tipo "DATA".
            # Por simplicidade, vamos considerar que datas são strings para EH/NAO_EH/CONTEM.
            # Se a variável é numérica, mas o operador espera string, ou vice versa
            if (expected_type == 'NUMERO' and actual_type == 'STRING') or (
                expected_type == 'STRING'
                and actual_type == 'NUMERO'
                and op_comparacao_token.type
                not in [
                    FileManagerParser.MAIOR_QUE,
                    FileManagerParser.MENOR_QUE,
                    FileManagerParser.IGUAL_OU_MAIOR_QUE,
                    FileManagerParser.IGUAL_OU_MENOR_QUE,
                ]
            ):
                self.errors.append(
                    f"Erro semântico: Comparação inválida entre {var_name} ({expected_type}) e '{value}' ({actual_type}) com operador '{operator_name}'."
                )
                return None

        # Verifica se um operador numérico está sendo usado com uma variável de string
        numeric_operators = [
            FileManagerParser.MAIOR_QUE,
            FileManagerParser.MENOR_QUE,
            FileManagerParser.IGUAL_OU_MAIOR_QUE,
            FileManagerParser.IGUAL_OU_MENOR_QUE,
        ]
        string_variables = [
            FileManagerParser.VAR_NOME,
            FileManagerParser.VAR_NOME_BASE,
            FileManagerParser.VAR_EXTENSAO,
            FileManagerParser.VAR_DATA_CRIACAO,
            FileManagerParser.VAR_DATA_MODIFICACAO,
            FileManagerParser.VAR_TIPO_MIME,
        ]

        if (
            op_comparacao_token.type in numeric_operators
            and var_metadata_token.type in string_variables
        ):
            self.errors.append(
                f"Erro semântico: Operador numérico '{operator_name}' usado com variável de string '{var_name}'."
            )
            return None

        # Verifica se um operador de string está sendo usado com uma variável numérica (com exceção de EH/NAO_EH que podem ser mais flexíveis)
        string_operators = [
            FileManagerParser.CONTEM,
            FileManagerParser.NAO_CONTEM,
            FileManagerParser.COMECA_COM,
            FileManagerParser.TERMINA_COM,
        ]
        numeric_variables = [
            FileManagerParser.VAR_TAMANHO_KB,
            FileManagerParser.VAR_TAMANHO_MB,
        ]

        if (
            op_comparacao_token.type in string_operators
            and var_metadata_token.type in numeric_variables
        ):
            self.errors.append(
                f"Erro semântico: Operador de string '{operator_name}' usado com variável numérica '{var_name}'."
            )
            return None

        return {
            'variable': var_name,
            'operator': operator_name,
            'value': value,
            'value_type': actual_type,  # Armazena o tipo real do valor para futura geração de script
        }

    def visitMoverPara(self, ctx: FileManagerParser.MoverParaContext):
        target_path = ctx.STRING().getText().strip('"')
        return {'action': 'move', 'target': target_path}

    def visitCopiarPara(self, ctx: FileManagerParser.CopiarParaContext):
        target_path = ctx.STRING().getText().strip('"')
        return {'action': 'copy', 'target': target_path}

    def visitRenomearPara(self, ctx: FileManagerParser.RenomearParaContext):
        # A gramática foi ajustada para usar STRING.
        # Aqui você pega a string bruta e lida com a interpolação posteriormente.
        new_name_template = ctx.STRING().getText().strip('"')
        return {'action': 'rename', 'new_name_template': new_name_template}

    def visitExcluir(self, ctx: FileManagerParser.ExcluirContext):
        return {'action': 'delete'}

    def visitAplicarTags(self, ctx: FileManagerParser.AplicarTagsContext):
        tags = []
        for string_ctx in ctx.listaTags().STRING():
            tags.append(string_ctx.getText().strip('"'))
        return {'action': 'apply_tags', 'tags': tags}
