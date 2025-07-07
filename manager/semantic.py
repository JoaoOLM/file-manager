import os
from .parser.FileManagerParser import FileManagerParser
from .parser.FileManagerVisitor import FileManagerVisitor
from datetime import datetime


class SemanticAnalyzer(FileManagerVisitor):
    def __init__(self):
        super().__init__()
        self.root_directory = None
        self.rules = []
        self.errors = []

        # Mapeamento de operadores para tipos compatíveis
        self.type_map = {
            FileManagerParser.EH: ["STRING", "NUMERO", "DATA"],
            FileManagerParser.NAO_EH: ["STRING", "NUMERO", "DATA"],
            FileManagerParser.CONTEM: ["STRING"],
            FileManagerParser.NAO_CONTEM: ["STRING"],
            FileManagerParser.COMECA_COM: ["STRING"],
            FileManagerParser.TERMINA_COM: ["STRING"],
            FileManagerParser.MAIOR_QUE: ["NUMERO", "DATA"],
            FileManagerParser.MENOR_QUE: ["NUMERO", "DATA"],
            FileManagerParser.IGUAL_OU_MAIOR_QUE: ["NUMERO", "DATA"],
            FileManagerParser.IGUAL_OU_MENOR_QUE: ["NUMERO", "DATA"],
        }

        # Mapeamento de variáveis de metadados para seus tipos esperados
        self.variable_types = {
            FileManagerParser.VAR_NOME: "STRING",
            FileManagerParser.VAR_NOME_BASE: "STRING",
            FileManagerParser.VAR_EXTENSAO: "STRING",
            FileManagerParser.VAR_TAMANHO_KB: "NUMERO",
            FileManagerParser.VAR_TAMANHO_MB: "NUMERO",
            FileManagerParser.VAR_DATA_CRIACAO: "DATA",
            FileManagerParser.VAR_DATA_MODIFICACAO: "DATA",
            FileManagerParser.VAR_TIPO_MIME: "STRING",
        }

        # Formato de data esperado (ex: 'YYYY-MM-DD')
        self.date_format = "%Y-%m-%d"

    # --- Funções Auxiliares para Parsing de Valores ---
    def _parse_string_value(self, valor_ctx):
        """Tenta parsear um contexto de STRING."""
        if valor_ctx.STRING():
            return valor_ctx.STRING().getText().strip('"'), "STRING", None
        return None, None, "Valor não é uma STRING."

    def _parse_numeric_value(self, valor_ctx):
        """Tenta parsear um contexto de NUMERO."""
        if valor_ctx.NUMERO():
            text_value = valor_ctx.NUMERO().getText()
            try:
                numeric_value = (
                    float(text_value) if "." in text_value else int(text_value)
                )
                return numeric_value, "NUMERO", None
            except ValueError:
                return None, None, f"Valor numérico inválido: '{text_value}'."
        return None, None, "Valor não é um NUMERO."

    def _parse_date_value(self, valor_ctx):
        """Tenta parsear um contexto de STRING como DATA."""
        if valor_ctx.STRING():
            text_value = valor_ctx.STRING().getText().strip('"')
            try:
                date_value = datetime.strptime(text_value, self.date_format)
                return date_value, "DATA", None
            except ValueError:
                return (
                    None,
                    None,
                    f"Formato de data inválido. Esperado '{self.date_format}', encontrado '{text_value}'.",
                )
        return None, None, "Valor não é uma STRING para ser tratada como DATA."

    def _parse_value(self, valor_ctx, expected_var_type):
        """
        Função despachante para parsear o valor literal baseado no tipo esperado.
        Retorna (valor_convertido, tipo_detectado, texto_original, mensagem_de_erro).
        """
        actual_value = None
        actual_value_type = None
        actual_value_text = None
        error_message = None

        if valor_ctx.STRING():
            actual_value_text = valor_ctx.STRING().getText().strip('"')
            if expected_var_type == "DATA":
                actual_value, actual_value_type, error_message = self._parse_date_value(
                    valor_ctx
                )
            else:  # STRING ou qualquer outro tipo que aceite STRING literal
                actual_value, actual_value_type, error_message = (
                    self._parse_string_value(valor_ctx)
                )
        elif valor_ctx.NUMERO():
            actual_value_text = valor_ctx.NUMERO().getText()
            if expected_var_type == "NUMERO":
                actual_value, actual_value_type, error_message = (
                    self._parse_numeric_value(valor_ctx)
                )
            else:
                # Caso de tipo incompatível detectado antes mesmo do parsing completo
                # (ex: variável STRING/DATA com literal NUMERO)
                error_message = f"Variável espera tipo '{expected_var_type}', mas valor fornecido é numérico '{actual_value_text}'."
                actual_value_type = (
                    "NUMERO"  # Define o tipo real para a mensagem de erro
                )
        else:
            error_message = "Valor inesperado na expressão booleana."

        return actual_value, actual_value_type, actual_value_text, error_message

    # Funções auxiliares para validar compatibilidade
    def _validate_operator_type_compatibility(
        self, op_type, var_type, value_type, var_name, operator_name, value_text
    ):
        compatible_types_for_operator = self.type_map.get(op_type)

        if not compatible_types_for_operator:
            self.errors.append(
                f"Erro semântico: Operador de comparação desconhecido: '{operator_name}'."
            )
            return False

        if var_type not in compatible_types_for_operator:
            self.errors.append(
                f"Erro semântico: Operador '{operator_name}' não é compatível com a variável '{var_name}' do tipo '{var_type}'."
            )
            return False

        if value_type not in compatible_types_for_operator:
            self.errors.append(
                f"Erro semântico: Valor de tipo '{value_type}' ('{value_text}') não é compatível com o operador '{operator_name}' e a variável '{var_name}' do tipo '{var_type}'."
            )
            return False

        # Casos específicos de erro de tipo mais detalhados
        numeric_operators = [
            FileManagerParser.MAIOR_QUE,
            FileManagerParser.MENOR_QUE,
            FileManagerParser.IGUAL_OU_MAIOR_QUE,
            FileManagerParser.IGUAL_OU_MENOR_QUE,
        ]
        string_comparison_operators = [
            FileManagerParser.CONTEM,
            FileManagerParser.NAO_CONTEM,
            FileManagerParser.COMECA_COM,
            FileManagerParser.TERMINA_COM,
        ]

        if var_type == "STRING" and op_type in numeric_operators:
            self.errors.append(
                f"Erro semântico: Operador numérico '{operator_name}' não pode ser usado com variável de string '{var_name}'."
            )
            return False

        if var_type == "NUMERO" and op_type in string_comparison_operators:
            self.errors.append(
                f"Erro semântico: Operador de string '{operator_name}' não pode ser usado com variável numérica '{var_name}'."
            )
            return False

        if var_type == "DATA" and op_type in string_comparison_operators:
            self.errors.append(
                f"Erro semântico: Operador de string '{operator_name}' não pode ser usado com variável de data '{var_name}'."
            )
            return False

        return True  # Tudo válido

    def visitPrograma(self, ctx: FileManagerParser.ProgramaContext):
        self.visit(ctx.declaracaoPastaRaiz())
        for regra_ctx in ctx.regra():
            self.visit(regra_ctx)

        return {
            "root_directory": self.root_directory,
            "rules": self.rules,
            "errors": self.errors,
        }

    def visitDeclaracaoPastaRaiz(
        self, ctx: FileManagerParser.DeclaracaoPastaRaizContext
    ):
        self.root_directory = ctx.STRING().getText().strip('"')
        if not os.path.isdir(self.root_directory):
            self.errors.append(
                f"Erro semântico: Pasta raiz '{self.root_directory}' não existe ou não é um diretório."
            )

    def visitRegra(self, ctx: FileManagerParser.RegraContext):
        current_rule = {"conditions": [], "actions": []}

        condition_result = self.visit(ctx.condicao())
        if condition_result:
            current_rule["conditions"] = condition_result

        for acao_ctx in ctx.acao():
            action_result = self.visit(acao_ctx)
            if action_result:
                current_rule["actions"].append(action_result)

        self.rules.append(current_rule)

    def visitCondicao(self, ctx: FileManagerParser.CondicaoContext):
        conditions = []
        for i, expr_ctx in enumerate(ctx.expressaoBooleana()):
            expr = self.visit(expr_ctx)
            # Se uma expressão tiver erro, ela retorna None, queremos propagar isso
            if expr is None:
                return (
                    None  # Aborta a coleta de condições para esta regra se houver erro
                )

            conditions.append(expr)

            if i < len(ctx.expressaoBooleana()) - 1:
                op_token = ctx.getChild(2 * i + 1)
                op_text = op_token.getText()
                conditions.append(op_text)
        return conditions

    def visitExpressaoBooleana(self, ctx: FileManagerParser.ExpressaoBooleanaContext):
        var_metadata_token = ctx.variavelMetadata().children[0].symbol
        op_comparacao_token = ctx.operadorComparacao().children[0].symbol
        valor_ctx = ctx.valor()

        var_name = var_metadata_token.text
        operator_name = op_comparacao_token.text

        expected_var_type = self.variable_types.get(var_metadata_token.type)
        if not expected_var_type:
            self.errors.append(
                f"Erro semântico: Variável de metadado desconhecida '{var_name}'."
            )
            return None

        # 1. Parse do Valor Literal
        actual_value, actual_value_type, actual_value_text, parse_error = (
            self._parse_value(valor_ctx, expected_var_type)
        )
        if parse_error:
            self.errors.append(f"Erro semântico: Para '{var_name}': {parse_error}")
            return None

        # 2. Validação de Compatibilidade de Tipos e Operadores
        is_valid = self._validate_operator_type_compatibility(
            op_comparacao_token.type,
            expected_var_type,
            actual_value_type,
            var_name,
            operator_name,
            actual_value_text,
        )
        if not is_valid:
            return None  # Erros já foram adicionados em _validate_operator_type_compatibility

        # Se tudo estiver OK, retorna os dados da expressão
        return {
            "variable": var_name,
            "operator": operator_name,
            "value": actual_value,
            "value_text": actual_value_text,
            "value_type": actual_value_type,
            "expected_var_type": expected_var_type,
        }

    def visitMoverPara(self, ctx: FileManagerParser.MoverParaContext):
        target_path = ctx.STRING().getText().strip('"')
        parent_dir = os.path.dirname(os.path.abspath(target_path))
        if not os.access(parent_dir, os.W_OK):
            self.errors.append(
                f"Aviso semântico: Não é possível criar o diretório de destino '{target_path}' para MOVER_PARA. Verifique permissões de escrita em '{parent_dir}'."
            )
        return {"action": "move", "target": target_path}

    def visitCopiarPara(self, ctx: FileManagerParser.CopiarParaContext):
        target_path = ctx.STRING().getText().strip('"')
        return {"action": "copy", "target": target_path}

    def visitRenomearPara(self, ctx: FileManagerParser.RenomearParaContext):
        new_name_template = ctx.STRING().getText().strip('"')
        return {"action": "rename", "new_name_template": new_name_template}

    def visitExcluir(self, ctx: FileManagerParser.ExcluirContext):
        return {"action": "delete"}

    def visitAplicarTags(self, ctx: FileManagerParser.AplicarTagsContext):
        tags = []
        for string_ctx in ctx.listaTags().STRING():
            tags.append(string_ctx.getText().strip('"'))
        return {"action": "apply_tags", "tags": tags}


def run_semantic(tree):
    """
    Executa a análise semântica na árvore de sintaxe fornecida e retorna os resultados.
    """
    semantic_analyzer = SemanticAnalyzer()
    semantic_result = semantic_analyzer.visit(tree)

    return semantic_result
