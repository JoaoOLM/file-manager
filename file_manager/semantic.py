import re 

from .parser.FileManagerVisitor import FileManagerVisitor
from .parser.FileManagerParser import FileManagerParser
from .error_handler import ErrorHandler

class SemanticAnalyzer(FileManagerVisitor):
    """
    Classe responsável por executar a análise semântica do programa.
    Percorre a árvore de sintaxe (Parse Tree) e verifica a correção lógica e de tipos.
    """
    def __init__(self, error_handler: ErrorHandler):
        super().__init__()
        self.error_handler = error_handler
        
        # Mapa para validar tipos de variáveis de metadados
        self.variable_types = {
            '$NOME': 'string',
            '$NOME_BASE': 'string',
            '$EXTENSAO': 'string',
            '$TAMANHO_KB': 'numeric',
            '$TAMANHO_MB': 'numeric',
            '$DATA_CRIACAO': 'date',
            '$DATA_MODIFICACAO': 'date',
            '$TIPO_MIME': 'string'
        }

        # Conjuntos de operadores válidos por tipo
        self.valid_string_operators = {'EH', 'NAO_EH', 'CONTEM', 'NAO_CONTEM', 'COMECA_COM', 'TERMINA_COM'}
        self.valid_numeric_operators = {'EH', 'NAO_EH', 'MAIOR_QUE', 'MENOR_QUE', 'IGUAL_OU_MAIOR_QUE', 'IGUAL_OU_MENOR_QUE'}
        self.valid_date_operators = {'EH', 'NAO_EH', 'MAIOR_QUE', 'MENOR_QUE', 'IGUAL_OU_MAIOR_QUE', 'IGUAL_OU_MENOR_QUE'}

        # Para detecção de conflitos de ações dentro da mesma regra
        self.current_rule_actions = []

    def analyze(self, tree: FileManagerParser.ProgramaContext):
        """
        Inicia a análise semântica percorrendo a árvore de sintaxe.
        """
        print("Iniciando Análise Semântica...")
        # Começa a visita da árvore a partir do nó raiz
        self.visit(tree)
        print("Análise Semântica concluída.")

    # --- Visitadores para Regras Específicas da Gramática ---

    def visitDeclaracaoPastaRaiz(self, ctx: FileManagerParser.DeclaracaoPastaRaizContext):
        """
        Verifica a validade do caminho declarado para PASTA_RAIZ.
        """
        # O token STRING contém o texto do caminho entre aspas.
        # getSymbol() para obter informações de linha/coluna.
        root_path_token = ctx.STRING().getSymbol()
        # Remove as aspas da string literal para validação
        root_path = root_path_token.text.strip('"') 
        
        # Verificação 1: Caminho não pode ser vazio
        if not root_path:
            self.error_handler.report_error(
                "Erro Semântico",
                "Caminho da PASTA_RAIZ não pode ser vazio.",
                root_path_token.line,
                root_path_token.column
            )
        
        # Verificação 2: Formato de caminho absoluto (ex: começa com '/' ou "C:\\")
        # Essa validação é simplificada e pode precisar de ajustes para multiplataforma robusta.
        # Para Windows (regex ex: C:\Users\ ou \\server\share), para Linux/macOS (regex ex: /home/user)
        is_windows_absolute = re.match(r'^[A-Za-z]:[\\/].*', root_path) or re.match(r'^\\\\[a-zA-Z0-9_.-]+\\[a-zA-Z0-9_.-]+.*', root_path)
        is_unix_absolute = root_path.startswith('/')

        if not (is_windows_absolute or is_unix_absolute):
             self.error_handler.report_error(
                "Erro Semântico",
                f"Formato de caminho inválido para PASTA_RAIZ: '{root_path}'. Use um caminho absoluto (ex: '/home/user/downloads' ou 'C:\\Users\\user\\Downloads').",
                root_path_token.line,
                root_path_token.column
            )
        
        return self.visitChildren(ctx) # Continua a visita aos filhos do nó

    def visitRegra(self, ctx: FileManagerParser.RegraContext):
        """
        Chamado ao entrar em uma nova regra. Reinicia o controle de ações
        e verifica conflitos após visitar todas as ações da regra.
        """
        # Reseta a lista de ações para a regra atual
        self.current_rule_actions = []
        
        # Visita todos os filhos desta regra (condições e ações)
        self.visitChildren(ctx) 
        
        # --- Verificações de Conflito de Ações dentro da Mesma Regra ---
        
        # 1. Conflito MOVER_PARA e EXCLUIR
        if 'MOVER_PARA' in self.current_rule_actions and 'EXCLUIR' in self.current_rule_actions:
            self.error_handler.report_error(
                "Erro Semântico",
                "Uma regra não pode conter as ações MOVER_PARA e EXCLUIR simultaneamente, pois são mutuamente exclusivas.",
                ctx.start.line, # Linha inicial da regra
                ctx.start.column
            )
        
        # 2. Múltiplas ações de movimento/cópia para diferentes destinos (potencial conflito de ordem)
        move_copy_actions = [a for a in self.current_rule_actions if a in ['MOVER_PARA', 'COPIAR_PARA']]
        if len(move_copy_actions) > 1:
            # Isso é mais um aviso, pois o comportamento dependerá da ordem de execução.
            # ANTLR processa da esquerda para a direita, então a última ação pode "ganhar".
            self.error_handler.report_error(
                "Aviso Semântico",
                "Múltiplas ações de movimento/cópia em uma única regra podem levar a comportamento ambíguo. A última ação definida prevalecerá.",
                ctx.start.line,
                ctx.start.column
            )
        
        return None # Retorna None ao invés de self.visitChildren(ctx) pois já visitamos os filhos

    def visitExpressaoBooleana(self, ctx: FileManagerParser.ExpressaoBooleanaContext):
        """
        Verifica a compatibilidade de tipos entre a variável de metadado, o operador
        e o valor na expressão booleana (e.g., $TAMANHO_KB MAIOR_QUE "texto").
        """
        var_name = ctx.variavelMetadata().getText() # Ex: '$TAMANHO_KB'
        operator = ctx.operadorComparacao().getText() # Ex: 'MAIOR_QUE'
        
        # Pega o token literal do valor para obter linha/coluna e o texto
        value_token = None
        if ctx.valor().STRING():
            value_token = ctx.valor().STRING().getSymbol()
        elif ctx.valor().NUMERO():
            value_token = ctx.valor().NUMERO().getSymbol()
        
        value_text = value_token.text if value_token else ctx.valor().getText() # Fallback

        expected_type = self.variable_types.get(var_name)
        
        if expected_type == 'string':
            # Verifica se o operador é válido para strings
            if operator not in self.valid_string_operators:
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Operador '{operator}' é inválido para variável de tipo STRING ('{var_name}').",
                    ctx.operadorComparacao().start.line,
                    ctx.operadorComparacao().start.column
                )
            # Verifica se o valor é uma string literal
            if not ctx.valor().STRING():
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Valor de comparação para '{var_name}' (STRING) deve ser uma string literal (entre aspas). Encontrado: '{value_text}'.",
                    value_token.line,
                    value_token.column
                )
        
        elif expected_type == 'numeric':
            # Verifica se o operador é válido para números
            if operator not in self.valid_numeric_operators:
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Operador '{operator}' é inválido para variável de tipo NUMÉRICO ('{var_name}').",
                    ctx.operadorComparacao().start.line,
                    ctx.operadorComparacao().start.column
                )
            # Verifica se o valor é um número literal
            if not ctx.valor().NUMERO():
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Valor de comparação para '{var_name}' (NUMÉRICO) deve ser um número. Encontrado: '{value_text}'.",
                    value_token.line,
                    value_token.column ignorados
                )
        
        elif expected_type == 'date':
            # Verifica se o operador é válido para datas
            if operator not in self.valid_date_operators:
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Operador '{operator}' é inválido para variável de tipo DATA ('{var_name}').",
                    ctx.operadorComparacao().start.line,
                    ctx.operadorComparacao().start.column
                )
            # Verifica se o valor é uma string literal (data é tratada como string)
            if not ctx.valor().STRING():
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Valor de comparação para '{var_name}' (DATA) deve ser uma string literal (entre aspas). Encontrado: '{value_text}'.",
                    value_token.line,
                    value_token.column
                )
            else:
                # Valida o formato da data (AAAA-MM-DD)
                date_str = value_token.text.strip('"')
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date_str):
                    self.error_handler.report_error(
                        "Erro Semântico",
                        f"Formato de data inválido para '{var_name}': '{date_str}'. Use o formato 'AAAA-MM-DD'.",
                        value_token.line,
                        value_token.column
                    )
        
        return self.visitChildren(ctx)

    def visitMoverPara(self, ctx: FileManagerParser.MoverParaContext):
        """
        Adiciona a ação MOVER_PARA à lista de ações da regra atual e valida o caminho.
        """
        self.current_rule_actions.append('MOVER_PARA')
        
        path_token = ctx.STRING().getSymbol()
        path = path_token.text.strip('"')

        # Verificação: Caminho não vazio
        if not path:
             self.error_handler.report_error(
                "Erro Semântico",
                "Caminho de destino para MOVER_PARA não pode ser vazio.",
                path_token.line,
                path_token.column
            )
        
        # Verificação: Formato de caminho absoluto (reutiliza a lógica da PASTA_RAIZ)
        is_windows_absolute = re.match(r'^[A-Za-z]:[\\/].*', path) or re.match(r'^\\\\[a-zA-Z0-9_.-]+\\[a-zA-Z0-9_.-]+.*', path)
        is_unix_absolute = path.startswith('/')

        if not (is_windows_absolute or is_unix_absolute):
             self.error_handler.report_error(
                "Erro Semântico",
                f"Formato de caminho inválido para MOVER_PARA: '{path}'. Use um caminho absoluto.",
                path_token.line,
                path_token.column
            )
        
        return self.visitChildren(ctx)

    def visitCopiarPara(self, ctx: FileManagerParser.CopiarParaContext):
        """
        Adiciona a ação COPIAR_PARA à lista de ações da regra atual e valida o caminho.
        """
        self.current_rule_actions.append('COPIAR_PARA')
        
        path_token = ctx.STRING().getSymbol()
        path = path_token.text.strip('"')

        if not path:
             self.error_handler.report_error(
                "Erro Semântico",
                "Caminho de destino para COPIAR_PARA não pode ser vazio.",
                path_token.line,
                path_token.column
            )
        
        is_windows_absolute = re.match(r'^[A-Za-z]:[\\/].*', path) or re.match(r'^\\\\[a-zA-Z0-9_.-]+\\[a-zA-Z0-9_.-]+.*', path)
        is_unix_absolute = path.startswith('/')

        if not (is_windows_absolute or is_unix_absolute):
             self.error_handler.report_error(
                "Erro Semântico",
                f"Formato de caminho inválido para COPIAR_PARA: '{path}'. Use um caminho absoluto.",
                path_token.line,
                path_token.column
            )
        return self.visitChildren(ctx)

    def visitRenomearPara(self, ctx: FileManagerParser.RenomearParaContext):
        """
        Adiciona a ação RENOMEAR_PARA e valida a string de renomeação.
        Verifica variáveis de metadados desconhecidas e caracteres inválidos.
        """
        self.current_rule_actions.append('RENOMEAR_PARA')
        
        rename_string_token = ctx.STRING().getSymbol()
        rename_string = rename_string_token.text.strip('"')

        # 1. Verificação de variáveis de metadados válidas dentro da string de renomeação
        # Regex para encontrar placeholders como ${VARIAVEL}
        matches = re.findall(r'\${([A-Z_]+)}', rename_string)
        for match in matches:
            # Converte o nome da variável encontrada para o formato de token (ex: DATA_MODIFICACAO -> $DATA_MODIFICACAO)
            var_token_name = f"${match}"
            if var_token_name not in self.variable_types:
                self.error_handler.report_error(
                    "Erro Semântico",
                    f"Variável de metadado desconhecida na string de renomeação: '${{{match}}}'.",
                    rename_string_token.line,
                    rename_string_token.column 
                )
        
        # 2. Validação de caracteres inválidos no nome resultante (simbólico, pois a substituição é em runtime)
        # Nomes de arquivos não podem ter: / \ ? % * : | " < >
        # A regex considera que a string de entrada NÃO terá as variáveis substituídas ainda.
        # Estamos procurando por caracteres proibidos que seriam LITERAIS na string de renomeação.
        # Ex: "meu:arquivo.txt" ou "pasta/arquivo.txt"
        forbidden_chars_regex = r'[\\/?%*:|"<>]+' # Caracteres comumente proibidos (um ou mais)
        # Excluímos os caracteres '$' e '{', '}' que fazem parte da sintaxe das variáveis,
        # para que o validador não reporte erro neles.
        clean_string_for_check = re.sub(r'\$\{[A-Z_]+\}', '', rename_string) # Remove os placeholders das variáveis para a verificação
        
        if re.search(forbidden_chars_regex, clean_string_for_check): 
            self.error_handler.report_error(
                "Erro Semântico",
                f"A string de renomeação '{rename_string}' contém caracteres que podem ser inválidos para nomes de arquivos (ex: \\ / ? % * : | \" < >).",
                rename_string_token.line,
                rename_string_token.column
            )

        return self.visitChildren(ctx)

    def visitExcluir(self, ctx: FileManagerParser.ExcluirContext):
        """
        Adiciona a ação EXCLUIR à lista de ações da regra atual.
        """
        self.current_rule_actions.append('EXCLUIR')
        return self.visitChildren(ctx)

    def visitAplicarTags(self, ctx: FileManagerParser.AplicarTagsContext):
        """
        Adiciona a ação APLICAR_TAGS e valida as tags.
        """
        self.current_rule_actions.append('APLICAR_TAGS')
        
        # As tags são uma lista de STRINGs
        tags_raw = [s.getText().strip('"') for s in ctx.listaTags().STRING()]
        
        for tag in tags_raw:
            if not tag: # Verifica se alguma tag está vazia (ex: "tag1", "", "tag3")
                self.error_handler.report_error(
                    "Erro Semântico",
                    "Tag vazia encontrada na ação APLICAR_TAGS. As tags não podem ser strings vazias.",
                    ctx.start.line, 
                    ctx.start.column + (ctx.getText().find('""') if '""' in ctx.getText() else 0) # Tenta estimar a coluna da tag vazia
                )
                    
        return self.visitChildren(ctx)