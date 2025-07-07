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

    # Função auxiliar para metadados de data para maior clareza no Bash
    # Isso encapsula a complexidade do `stat`
    script_parts.append("get_file_dates() {")
    script_parts.append("    local FILE_PATH=\"$1\"")
    script_parts.append("    local CREATION_DATE_FORMATTED=\"UNKNOWN_DATE\"")
    script_parts.append("    local MODIFICATION_DATE_FORMATTED=\"UNKNOWN_DATE\"")
    script_parts.append("")
    script_parts.append("    # Tenta GNU stat (Linux)")
    script_parts.append("    if command -v stat &>/dev/null && stat -c %w \"$FILE_PATH\" &>/dev/null; then")
    script_parts.append("        CREATION_DATE_TS=$(stat -c %W \"$FILE_PATH\")")
    script_parts.append("        MODIFICATION_DATE_TS=$(stat -c %Y \"$FILE_PATH\")")
    script_parts.append("        CREATION_DATE_FORMATTED=$(date -d @\"$CREATION_DATE_TS\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("        MODIFICATION_DATE_FORMATTED=$(date -d @\"$MODIFICATION_DATE_TS\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("    # Tenta BSD stat (macOS)")
    script_parts.append("    elif command -v stat &>/dev/null && stat -f %B \"$FILE_PATH\" &>/dev/null; then")
    script_parts.append("        CREATION_DATE_TS=$(stat -f %B \"$FILE_PATH\")")
    script_parts.append("        MODIFICATION_DATE_TS=$(stat -f %m \"$FILE_PATH\")")
    script_parts.append("        CREATION_DATE_FORMATTED=$(date -r \"$CREATION_DATE_TS\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("        MODIFICATION_DATE_FORMATTED=$(date -r \"$MODIFICATION_DATE_TS\" +\"%Y-%m-%d\" 2>/dev/null || echo \"UNKNOWN_DATE\")")
    script_parts.append("    fi")
    script_parts.append("    echo \"$CREATION_DATE_FORMATTED $MODIFICATION_DATE_FORMATTED\"") # Retorna as datas
    script_parts.append("}")
    script_parts.append("")

    # Loop principal para encontrar arquivos (recursivo por padrão)
    script_parts.append("find \"$ROOT_DIR\" -type f -print0 | while IFS= read -r -d $'\\0' FILE;")
    script_parts.append("do")
    script_parts.append("    echo \"\\n--- [INFO] Processando arquivo: $FILE ---\"")

    # Extração de metadados no Bash
    script_parts.append("    FILENAME=$(basename \"$FILE\")")
    script_parts.append("    BASENAME=\"${FILENAME%.*}\"")
    script_parts.append("    EXTENSION=\"${FILENAME##*.}\"")
    script_parts.append("    SIZE_KB=$(du -k \"$FILE\" | cut -f1 || echo 0)") # Fallback para 0 se du falhar
    script_parts.append("    SIZE_MB=$((SIZE_KB / 1024))")
    
    script_parts.append("    DATES=($(get_file_dates \"$FILE\"))") # Chama a função auxiliar
    script_parts.append("    CREATION_DATE_FORMATTED=\"${DATES[0]}\"")
    script_parts.append("    MODIFICATION_DATE_FORMATTED=\"${DATES[1]}\"")

    script_parts.append("    MIME_TYPE=$(file -b --mime-type \"$FILE\" 2>/dev/null || echo \"application/octet-stream\")") # Fallback
    
    script_parts.append("    echo \"      [DEBUG] Metadados: Nome='$FILENAME', Ext='$EXTENSION', Tamanho_KB='$SIZE_KB', Tamanho_MB='$SIZE_MB', Data_Criacao='$CREATION_DATE_FORMATTED', Data_Modif='$MODIFICATION_DATE_FORMATTED', Tipo_MIME='$MIME_TYPE'\"")
    script_parts.append("")

    for rule in semantic_data["rules"]:
        conditions_bash = []
        for i, part in enumerate(rule["conditions"]):
            if isinstance(part, str) and (part == "E" or part == "OU"):
                if part == "E":
                    conditions_bash.append(" && ")
                elif part == "OU":
                    conditions_bash.append(" || ")
            else: # É uma expressão booleana (dicionário)
                var_name = part["variable"]
                operator_name = part["operator"]
                value_text = part["value_text"] # Usar o texto original para comparações Bash

                bash_var_map = {
                    "$NOME": "FILENAME",
                    "$NOME_BASE": "BASENAME",
                    "$EXTENSAO": "EXTENSION",
                    "$TAMANHO_KB": "SIZE_KB",
                    "$TAMANHO_MB": "SIZE_MB",
                    "$DATA_CRIACAO": "CREATION_DATE_FORMATTED",
                    "$DATA_MODIFICACAO": "MODIFICATION_DATE_FORMATTED",
                    "$TIPO_MIME": "MIME_TYPE",
                }
                bash_var_name = bash_var_map.get(var_name, var_name.strip('$'))

                condition_str = ""
                
                # Usando ${VAR_NAME} para clareza e evitar problemas de expansão
                if operator_name == "EH":
                    condition_str = f"\"${{{bash_var_name}}}\" = \"{escape_bash_string(str(value_text))}\""
                elif operator_name == "NAO_EH":
                    condition_str = f"\"${{{bash_var_name}}}\" != \"{escape_bash_string(str(value_text))}\""
                elif operator_name == "CONTEM":
                    condition_str = f"\"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}*\""
                elif operator_name == "NAO_CONTEM":
                    condition_str = f"! \"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}*\""
                elif operator_name == "COMECA_COM":
                    condition_str = f"\"${{{bash_var_name}}}\" == \"{escape_bash_string(str(value_text))}*\""
                elif operator_name == "TERMINA_COM":
                    condition_str = f"\"${{{bash_var_name}}}\" == *\"{escape_bash_string(str(value_text))}\""
                elif operator_name in ["MAIOR_QUE", "MENOR_QUE", "IGUAL_OU_MAIOR_QUE", "IGUAL_OU_MENOR_QUE"]:
                    bash_op_map = {
                        "MAIOR_QUE": "-gt",
                        "MENOR_QUE": "-lt",
                        "IGUAL_OU_MAIOR_QUE": "-ge",
                        "IGUAL_OU_MENOR_QUE": "-le",
                    }
                    val_to_compare_escaped = escape_bash_string(str(value_text)) # Escapa o valor também
                    condition_str = f"\"${{{bash_var_name}}}\" {bash_op_map[operator_name]} \"{val_to_compare_escaped}\""
                
                conditions_bash.append(f"[[ {condition_str} ]]")

        script_parts.append(f"    if {' '.join(conditions_bash)}; then")
        script_parts.append("        echo \"      [INFO] Condição da REGRA satisfeita para $FILENAME\"")
        
        # Gerar ações
        for action in rule["actions"]:
            action_type = action["action"]
            if action_type == "move":
                target = action["target"]
                target_escaped = escape_bash_string(target)
                script_parts.append(f"        echo \"        [AÇÃO] Movendo '$FILENAME' para '{target}'\"")
                script_parts.append(f"        mkdir -p \"{target_escaped}\"")
                script_parts.append(f"        mv -v \"$FILE\" \"{target_escaped}/\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao mover '$FILENAME'.\" >&2") # mv -v para verbose, redireciona stderr para stdout e formata
            elif action_type == "copy":
                target = action["target"]
                target_escaped = escape_bash_string(target)
                script_parts.append(f"        echo \"        [AÇÃO] Copiando '$FILENAME' para '{target}'\"")
                script_parts.append(f"        mkdir -p \"{target_escaped}\"")
                script_parts.append(f"        cp -v \"$FILE\" \"{target_escaped}/\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao copiar '$FILENAME'.\" >&2") # cp -v para verbose
            elif action_type == "rename":
                new_name_template = action["new_name_template"]
                
                # Substituição dos placeholders da linguagem para variáveis Bash.
                # A ordem importa para evitar substituições parciais.
                interpolated_new_name_bash = new_name_template
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$NOME_BASE', '${BASENAME}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$EXTENSAO', '${EXTENSION}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$NOME', '${FILENAME}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$TAMANHO_KB', '${SIZE_KB}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$TAMANHO_MB', '${SIZE_MB}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$DATA_CRIACAO', '${CREATION_DATE_FORMATTED}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$DATA_MODIFICACAO', '${MODIFICATION_DATE_FORMATTED}')
                interpolated_new_name_bash = interpolated_new_name_bash.replace('$TIPO_MIME', '${MIME_TYPE}')

                script_parts.append(f"        NEW_FILE_NAME=\"{escape_bash_string(interpolated_new_name_bash)}\"")
                script_parts.append("        NEW_FILE_PATH=$(dirname \"$FILE\")/$NEW_FILE_NAME")
                script_parts.append("        echo \"        [AÇÃO] Renomeando '$FILENAME' para '$NEW_FILE_NAME'\"")
                script_parts.append("        mv -v \"$FILE\" \"$NEW_FILE_PATH\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao renomear '$FILENAME'.\" >&2")
            elif action_type == "delete":
                script_parts.append("        echo \"        [AÇÃO] Excluindo '$FILENAME'\"")
                script_parts.append("        rm -v \"$FILE\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao excluir '$FILENAME'.\" >&2")
            elif action_type == "apply_tags":
                tags = [escape_bash_string(tag) for tag in action["tags"]]
                tags_prefix = ""
                for tag in tags:
                    tags_prefix += f"[{tag}]"
                
                script_parts.append(f"        echo \"        [AÇÃO] Tentando aplicar tags [{', '.join(tags)}] ao nome de '$FILENAME'\"")
                script_parts.append(f"        if [[ \"$BASENAME\" == \"{tags_prefix}*\" ]]; then")
                script_parts.append(f"            echo \"          [INFO] '$FILENAME' já possui as tags '{', '.join(tags)}'. Pulando renomeação.\"")
                script_parts.append("        else")
                script_parts.append(f"            NEW_FILE_NAME=\"{tags_prefix}$BASENAME.$EXTENSION\"")
                script_parts.append("            NEW_FILE_PATH=$(dirname \"$FILE\")/$NEW_FILE_NAME")
                script_parts.append("            echo \"          Renomeando '$FILENAME' para '$NEW_FILE_NAME'\"")
                script_parts.append("            mv -v \"$FILE\" \"$NEW_FILE_PATH\" 2>&1 | sed 's/^/            /' || echo \"[ERRO] Falha ao aplicar tags a '$FILENAME'.\" >&2")
                script_parts.append("        fi")

        script_parts.append("    fi")
        script_parts.append("")
    
    script_parts.append("done")
    script_parts.append("echo \"[INFO] Processamento de arquivos concluído.\"")

    return "\n".join(script_parts)