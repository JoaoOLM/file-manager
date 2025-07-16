def escape_bash_string(s: str) -> str:
    """
    Escapa caracteres especiais em strings para uso seguro no Bash.
    Isso é crucial para caminhos de arquivo e nomes que podem conter espaços ou caracteres especiais.
    """
    # Escapa aspas duplas, cifrões (para evitar expansão indesejada de variáveis),
    # acentos graves (para evitar execução de comandos), e barras invertidas literais.
    return s.replace('"', '\\"').replace('$', '\\$').replace('`', '\\`').replace('\\', '\\\\')

def generate_bash_script(semantic_data: dict) -> str:
    """
    Gera um script Bash a partir dos dados da análise semântica.
    """
    script_parts = []
    
    # Shebang e opções de robustez
    script_parts.append("#!/bin/bash")
    script_parts.append("set -euo pipefail") # -u: erro se variável não definida; -e: sair em erro; -o pipefail: erro em pipeline
    script_parts.append("")
    
    root_dir = semantic_data.get("root_directory")
    if not root_dir:
        # Se root_dir não for válido, gera um script que apenas informa o erro.
        script_parts.append("echo \"[ERRO] A pasta raiz não foi definida ou é inválida na configuração. Abortando.\" >&2")
        script_parts.append("exit 1")
        return "\n".join(script_parts)

    script_parts.append(f"ROOT_DIR=\"{escape_bash_string(root_dir)}\"")
    script_parts.append("echo \"[INFO] Iniciando processamento de arquivos em: $ROOT_DIR\"")
    script_parts.append("")

    # Função auxiliar para obter metadados de data e timestamp de forma robusta no Bash
    script_parts.append("get_file_dates() {")
    script_parts.append("    local FILE_PATH=\"$1\"")
    script_parts.append("    local CREATION_DATE_TS_VAL=\"0\" # Default para timestamp 0 (1970-01-01)")
    script_parts.append("    local MODIFICATION_DATE_TS_VAL=\"0\"")
    script_parts.append("    local CREATION_DATE_FORMATTED=\"UNKNOWN_DATE\"")
    script_parts.append("    local MODIFICATION_DATE_FORMATTED=\"UNKNOWN_DATE\"")
    script_parts.append("")
    
    script_parts.append("    local GNU_STAT_W_OUTPUT=$(stat -c %W \"$FILE_PATH\" 2>/dev/null || echo \"0\")") # Creation timestamp (GNU)
    script_parts.append("    local GNU_STAT_Y_OUTPUT=$(stat -c %Y \"$FILE_PATH\" 2>/dev/null || echo \"0\")") # Modification timestamp (GNU)
    script_parts.append("    local BSD_STAT_B_OUTPUT=$(stat -f %B \"$FILE_PATH\" 2>/dev/null || echo \"0\")") # Creation timestamp (BSD)
    script_parts.append("    local BSD_STAT_M_OUTPUT=$(stat -f %m \"$FILE_PATH\" 2>/dev/null || echo \"0\")") # Modification timestamp (BSD)

    script_parts.append("    # Tenta GNU stat (Linux) e GNU date")
    script_parts.append("    if command -v stat &>/dev/null && [[ \"$GNU_STAT_W_OUTPUT\" != \"0\" ]] && command -v date &>/dev/null; then")
    script_parts.append("        CREATION_DATE_TS_VAL=\"$GNU_STAT_W_OUTPUT\"")
    script_parts.append("        MODIFICATION_DATE_TS_VAL=\"$GNU_STAT_Y_OUTPUT\"")
    script_parts.append("        CREATION_DATE_FORMATTED=$(date -d @\"$CREATION_DATE_TS_VAL\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("        MODIFICATION_DATE_FORMATTED=$(date -d @\"$MODIFICATION_DATE_TS_VAL\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("    # Tenta BSD stat (macOS) e BSD date")
    script_parts.append("    elif command -v stat &>/dev/null && [[ \"$BSD_STAT_B_OUTPUT\" != \"0\" ]] && command -v date &>/dev/null; then")
    script_parts.append("        CREATION_DATE_TS_VAL=\"$BSD_STAT_B_OUTPUT\"")
    script_parts.append("        MODIFICATION_DATE_TS_VAL=\"$BSD_STAT_M_OUTPUT\"")
    script_parts.append("        CREATION_DATE_FORMATTED=$(date -r \"$CREATION_DATE_TS_VAL\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("        MODIFICATION_DATE_FORMATTED=$(date -r \"$MODIFICATION_DATE_TS_VAL\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("    fi")
    # Retorna datas formatadas e timestamps. Use IFS para ler na chamada.
    script_parts.append("    echo \"$CREATION_DATE_FORMATTED $MODIFICATION_DATE_FORMATTED $CREATION_DATE_TS_VAL $MODIFICATION_DATE_TS_VAL\"")
    script_parts.append("}")
    script_parts.append("")

    # Loop principal para encontrar arquivos (recursivo por padrão)
    script_parts.append("find \"$ROOT_DIR\" -type f -print0 | while IFS= read -r -d $'\\0' FILE;")
    script_parts.append("do")
    script_parts.append("    echo \"\\n--- [INFO] Processando arquivo: $FILE ---\"")

    # Flag para controlar se o arquivo foi movido/excluído nesta iteração
    script_parts.append("    FILE_PROCESSED_AND_MOVED=false")

    # Verifica se o caminho do arquivo é válido antes de prosseguir
    script_parts.append("    if [[ -z \"$FILE\" ]]; then")
    script_parts.append("        echo \"      [AVISO] Caminho de arquivo vazio ou inválido. Pulando.\" >&2")
    script_parts.append("        continue") # Pula para a próxima iteração do loop find
    script_parts.append("    fi")

    # Extração de metadados no Bash
    script_parts.append("    FILENAME=$(basename \"$FILE\")")
    script_parts.append("    BASENAME=\"${FILENAME%.*}\"")
    script_parts.append("    EXTENSION=\"${FILENAME##*.}\"")
    script_parts.append("    SIZE_KB=$(du -k \"$FILE\" | cut -f1 || echo 0)") # Fallback para 0 se du falhar
    script_parts.append("    SIZE_MB=$((SIZE_KB / 1024))")
    
    script_parts.append("    DATES=($(get_file_dates \"$FILE\"))") # Chama a função auxiliar
    script_parts.append("    CREATION_DATE_FORMATTED=\"${DATES[0]}\"")
    script_parts.append("    MODIFICATION_DATE_FORMATTED=\"${DATES[1]}\"")
    script_parts.append("    CREATION_DATE_TS=\"${DATES[2]}\"") # Timestamp de criação
    script_parts.append("    MODIFICATION_DATE_TS=\"${DATES[3]}\"") # Timestamp de modificação

    script_parts.append("    MIME_TYPE=$(file -b --mime-type \"$FILE\" 2>/dev/null || echo \"application/octet-stream\")") # Fallback
    
    script_parts.append("    echo \"      [DEBUG] Metadados: Nome='$FILENAME', Ext='$EXTENSION', Tamanho_KB='$SIZE_KB', Tamanho_MB='$SIZE_MB', Data_Criacao='$CREATION_DATE_FORMATTED' (TS:$CREATION_DATE_TS), Data_Modif='$MODIFICATION_DATE_FORMATTED' (TS:$MODIFICATION_DATE_TS), Tipo_MIME='$MIME_TYPE'\"")
    script_parts.append("")

    for rule in semantic_data["rules"]:
        script_parts.append("    if $FILE_PROCESSED_AND_MOVED; then")
        script_parts.append("        echo \"      [INFO] Arquivo já foi movido/excluído por uma regra anterior. Pulando regras subsequentes para este arquivo.\"")
        script_parts.append("        continue") 
        script_parts.append("    fi")

        conditions_bash_parts = []
        current_or_group = []

        # Itera sobre as partes da condição para agrupar as expressões OU antes dos E
        for i, part in enumerate(rule["conditions"]):
            if isinstance(part, str) and (part == "E" or part == "OU"):
                if part == "E":
                    # Se há um grupo de ORs, fecha-o com parênteses e adiciona ao grupo principal
                    if current_or_group:
                        conditions_bash_parts.append(f"( {' '.join(current_or_group)} )")
                        current_or_group = []
                    conditions_bash_parts.append(" && ") # Adiciona o AND
                elif part == "OU":
                    if current_or_group:
                        current_or_group.append(" || ") # Adiciona o OR
            else: # É uma expressão booleana (dicionário)
                var_name = part["variable"]
                operator_name = part["operator"]
                value_text = part["value_text"] # Usar o texto original para comparações Bash
                
                # Detectar se a variável é de data e o operador é numérico para usar timestamp
                is_date_comparison = (var_name in ["$DATA_CRIACAO", "$DATA_MODIFICACAO"] and \
                                      operator_name in ["MAIOR_QUE", "MENOR_QUE", "IGUAL_OU_MAIOR_QUE", "IGUAL_OU_MENOR_QUE"])

                bash_var_map = {
                    "$NOME": "FILENAME", "$NOME_BASE": "BASENAME", "$EXTENSAO": "EXTENSION",
                    "$TAMANHO_KB": "SIZE_KB", "$TAMANHO_MB": "SIZE_MB",
                    # Mapear para timestamps se for uma comparação numérica de data
                    "$DATA_CRIACAO": "CREATION_DATE_TS", "$DATA_MODIFICACAO": "MODIFICATION_DATE_TS",
                    "$TIPO_MIME": "MIME_TYPE",
                }
                bash_var_name = bash_var_map.get(var_name, var_name.strip('$'))

                condition_str = ""
                
                if operator_name == "EH":
                    condition_str = f"\"${{{bash_var_name}}}\" = \"{escape_bash_string(str(value_text))}\""
                elif operator_name == "NAO_EH":
                    condition_str = f"\"${{{bash_var_name}}}\" != \"{escape_bash_string(str(value_text))}\""
                elif operator_name == "CONTEM":
                    condition_str = f"\"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}\"*"
                elif operator_name == "NAO_CONTEM":
                    condition_str = f"! [[ \"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}\"* ]]"
                elif operator_name == "COMECA_COM":
                    condition_str = f"\"${{{bash_var_name}}}\" == \"{escape_bash_string(str(value_text))}\"*"
                elif operator_name == "TERMINA_COM":
                    condition_str = f"\"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}\""
                elif operator_name in ["MAIOR_QUE", "MENOR_QUE", "IGUAL_OU_MAIOR_QUE", "IGUAL_OU_MENOR_QUE"]:
                    bash_op_map = {
                        "MAIOR_QUE": "-gt", "MENOR_QUE": "-lt",
                        "IGUAL_OU_MAIOR_QUE": "-ge", "IGUAL_OU_MENOR_QUE": "-le",
                    }
                    val_to_compare_escaped = escape_bash_string(str(value_text))
                    
                    if is_date_comparison:
                        # Converte a data string (ex: "2024-01-01") para timestamp Unix no Bash
                        # Tenta GNU date (-d) e depois BSD date (-j -f)
                        condition_str = f"\"${{{bash_var_name}}}\" {bash_op_map[operator_name]} $(date -d \"{val_to_compare_escaped}\" +%s 2>/dev/null || date -j -f \"%Y-%m-%d\" \"{val_to_compare_escaped}\" \"+%s\" 2>/dev/null || echo \"0\")"
                    else: # Comparação de número normal
                        condition_str = f"\"${{{bash_var_name}}}\" {bash_op_map[operator_name]} \"{val_to_compare_escaped}\""
                
                current_or_group.append(f"[[ {condition_str} ]]")
        
        # Adiciona o último grupo de ORs ao grupo principal de condições, se houver
        if current_or_group:
            conditions_bash_parts.append(f"( {' '.join(current_or_group)} )")

        # Inicia o bloco IF para a regra
        script_parts.append(f"    if {' '.join(conditions_bash_parts)}; then")
        script_parts.append("        echo \"      [INFO] Condição da REGRA satisfeita para $FILENAME\"")

        # Gerar ações
        for action in rule["actions"]:
            action_type = action["action"]
            
            if action_type == "move":
                target = action["target"]
                target_escaped = escape_bash_string(target)
                script_parts.append(f"        echo \"        [AÇÃO] Movendo '$FILENAME' para '{target}'\"")
                script_parts.append(f"        mkdir -p \"{target_escaped}\"")
                # Usa 'if mv -v ...; then' para capturar o sucesso e setar a flag
                script_parts.append(f"        if mv -v \"$FILE\" \"{target_escaped}/\" 2>&1 | sed 's/^/            /'; then")
                script_parts.append(f"            FILE=\"{target_escaped}/$FILENAME\"") # Atualiza FILE para o novo local
                script_parts.append("            echo \"            [INFO] Arquivo movido com sucesso. Atualizando caminho.\"")
                script_parts.append("        else")
                script_parts.append("            echo \"[ERRO] Falha ao mover '$FILENAME'.\" >&2")
                script_parts.append("            continue") # Pula para o próximo arquivo se o movimento falhar
                script_parts.append("        fi")
            elif action_type == "copy":
                target = action["target"]
                target_escaped = escape_bash_string(target)
                script_parts.append(f"        echo \"        [AÇÃO] Copiando '$FILENAME' para '{target}'\"")
                script_parts.append(f"        mkdir -p \"{target_escaped}\"")
                script_parts.append(f"        cp -v \"$FILE\" \"{target_escaped}/\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao copiar '$FILENAME'.\" >&2")
            elif action_type == "rename":
                new_name_template = action["new_name_template"]
                
                # Substituição dos placeholders da linguagem para variáveis Bash.
                interpolated_new_name_bash = new_name_template
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${NOME_BASE}', '${BASENAME}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${EXTENSAO}', '${EXTENSION}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${NOME}', '${FILENAME}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${TAMANHO_KB}', '${SIZE_KB}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${TAMANHO_MB}', '${SIZE_MB}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${DATA_CRIACAO}', '${CREATION_DATE_FORMATTED}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${DATA_MODIFICACAO}', '${MODIFICATION_DATE_FORMATTED}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('${TIPO_MIME}', '${MIME_TYPE}')

                script_parts.append(f"        NEW_FILE_NAME=\"{interpolated_new_name_bash}\"")
                script_parts.append("        NEW_FILE_PATH=$(dirname \"$FILE\")/$NEW_FILE_NAME")
                script_parts.append("        echo \"        [AÇÃO] Renomeando '$FILENAME' para '$NEW_FILE_NAME'\"")
                script_parts.append("        if mv -v \"$FILE\" \"$NEW_FILE_PATH\" 2>&1 | sed 's/^/            /'; then")
                script_parts.append("            FILE=\"$NEW_FILE_PATH\"") # Atualiza a variável FILE para ações subsequentes na mesma regra
                script_parts.append("            FILENAME=$(basename \"$FILE\")") # Re-extrai metadados
                script_parts.append("            BASENAME=\"${FILENAME%.*}\"")
                script_parts.append("            EXTENSION=\"${FILENAME##*.}\"")
                script_parts.append("        else")
                script_parts.append("            echo \"[ERRO] Falha ao renomear '$FILENAME'.\" >&2")
                script_parts.append("        fi")
            elif action_type == "delete":
                script_parts.append("        echo \"        [AÇÃO] Excluindo '$FILENAME'\"")
                script_parts.append("        if rm -v \"$FILE\" 2>&1 | sed 's/^/            /'; then")
                script_parts.append("            echo \"            [INFO] Arquivo excluído com sucesso.\"")
                script_parts.append("        else")
                script_parts.append("            echo \"[ERRO] Falha ao excluir '$FILENAME'.\" >&2")
                script_parts.append("        fi")
            elif action_type == "apply_tags":
                tags = [escape_bash_string(tag) for tag in action["tags"]]
                tags_prefix = ""
                for tag in tags:
                    tags_prefix += f"[{tag}]"
                
                script_parts.append(f"        echo \"        [AÇÃO] Tentando aplicar tags [{', '.join(tags)}] ao nome de '$FILENAME'\"")
                
                script_parts.append(f"        if [[ \"${{BASENAME}}\" == \"{tags_prefix}\"* ]]; then")
                script_parts.append(f"            echo \"          [INFO] '$FILENAME' já possui as tags '{', '.join(tags)}'. Pulando renomeação.\"")
                script_parts.append("        else")
                script_parts.append(f"            NEW_FILE_NAME=\"{tags_prefix}$BASENAME.$EXTENSION\"")
                script_parts.append("            NEW_FILE_PATH=$(dirname \"$FILE\")/$NEW_FILE_NAME")
                script_parts.append("            echo \"          Renomeando '$FILENAME' para '$NEW_FILE_NAME'\"")
                script_parts.append("            if mv -v \"$FILE\" \"$NEW_FILE_PATH\" 2>&1 | sed 's/^/            /'; then")
                script_parts.append("                FILE=\"$NEW_FILE_PATH\"") # Atualiza FILE para ações subsequentes na mesma regra
                script_parts.append("                FILENAME=$(basename \"$FILE\")") # Re-extrai metadados
                script_parts.append("                BASENAME=\"${FILENAME%.*}\"")
                script_parts.append("                EXTENSION=\"${FILENAME##*.}\"")
                script_parts.append("            else")
                script_parts.append("                echo \"[ERRO] Falha ao aplicar tags a '$FILENAME'.\" >&2")
                script_parts.append("            fi")
                script_parts.append("        fi")

        # Marca que o arquivo foi processado por uma regra após todas as ações
        script_parts.append("        FILE_PROCESSED_AND_MOVED=true")
        script_parts.append("    fi")
        script_parts.append("") # Linha em branco para legibilidade
    
    script_parts.append("done")
    script_parts.append("echo \"[INFO] Processamento de arquivos concluído.\"")

    return "\n".join(script_parts)