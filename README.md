# FileManager: Seu Compilador de Organização de Arquivos

O **FileManager** é um compilador de código aberto projetado para automatizar e simplificar a organização de arquivos em sistemas Linux/Unix. Cansado de mover, renomear e excluir arquivos manualmente? Com o FileManager, você define regras claras em uma linguagem intuitiva, e o compilador gera um script Bash executável que faz o trabalho pesado para você.

---

## Como o FileManager Funciona?

O FileManager opera através de um processo de compilação em fases, transformando suas regras de alto nível em um script Bash eficiente:

1.  **Análise Léxica:** A entrada (seu arquivo `.fm` com as regras) é quebrada em **tokens** (as "palavras" da linguagem, como `PASTA_RAIZ`, `$NOME`, `EH`, `STRING`).
2.  **Análise Sintática:** Os tokens são validados contra as regras gramaticais da linguagem, construindo uma **Árvore de Sintaxe Abstrata (AST)** que representa a estrutura do seu programa.
3.  **Análise Semântica:** A AST é percorrida para verificar a lógica do programa. Isso inclui a **verificação de tipos** (ex: garantir que você não esteja comparando um tamanho de arquivo com uma string de texto usando um operador numérico), a validação de caminhos e a garantia de que as operações fazem sentido. **Erros semânticos** são capturados aqui.
4.  **Geração de Código:** Se o programa for semanticamente válido, o compilador gera um **script Bash** (`file_manager_script.sh`) que implementa suas regras. Esse script pode então ser executado diretamente no seu terminal para organizar seus arquivos.

---

## Instalação e Execução

Para começar a usar o FileManager, siga os passos abaixo. Você precisará ter o **Python 3.11+** e o gerenciador de pacotes `uv` (recomendado) ou `pip` instalados em seu sistema.

<details>
<summary><strong> Setup do projeto </strong></summary>

### 1. Clonar o Repositório

```bash
git clone https://github.com/JoaoOLM/file-manager.git
cd file-manager
``` 

### 2. Instalar as dependências 

#### Dado que você so tem pip 😔
> O python 3.13 deve estar instalado na sua maquina se for seguir esse caminho 
ou baixar via [pyenv](https://github.com/pyenv/pyenv) 

- Criar o ambiente virtual
```bash
python -m venv .venv
```
- Ativar o ambiente virtual
```bash
source .venv/bin/activate
```
- Baixar as dependências do projeto
```bash
pip install .
```
#### Se voce tiver o [uv](https://docs.astral.sh/uv/) 😊
- Basta rodar
```bash
uv sync
```
- Depois entrar no ambiente virtual
```bash
source .venv/bin/activate
```

### 3. Executar o Compilador

Para compilar um arquivo de regras .fm e gerar o script Bash, use o comando uv run manager seguido pelo caminho do seu arquivo de regras:

```bash
manager compiler <caminho/para/seu_arquivo_de_regras.fm>
```

Exemplo:

```bash
manager compiler tests/move_pdf_large.fm
```

### 4. Executar o Script Bash Gerado

Após a compilação, um script Bash chamado file_manager_script.sh será gerado no diretório raiz do seu projeto. Você pode executá-lo diretamente:

```bash
./file_manager_script.sh
```

**Atenção:** Tenha muito cuidado ao executar scripts que manipulam arquivos. É altamente recomendável testar em um diretório de arquivos de teste (~/TestFiles/) antes de aplicar em pastas com dados importantes.

</details>

## Guia da Gramática da Linguagem FileManager

A linguagem **FileManager** é simples e direta, projetada para expressar regras de organização de arquivos de forma clara.

<details>
<summary><strong> Documentação da linguagem </strong></summary>

### Estrutura Básica de um Programa

Todo programa FileManager começa com a declaração da pasta raiz, seguida por uma ou mais regras:

```fm
PASTA_RAIZ "/caminho/do/diretorio";

REGRA SE <condicao> ENTAO <acao_1> (E <acao_2>)*;
```

**Atenção:** a pasta raiz deve começar com barra e deve ser um arquivo já existente.

---

### Palavras-Chave

As palavras-chave são os elementos fundamentais da linguagem:

- **PASTA_RAIZ**: Define o diretório base para todas as operações.
- **REGRA**: Inicia a definição de uma nova regra de automação.
- **SE**: Introduz a(s) condição(ões) da regra.
- **E**: Operador lógico AND para combinar condições ou ações.
- **OU**: Operador lógico OR para combinar condições.
- **ENTAO**: Separa a(s) condição(ões) da(s) ação(ões).
- **MOVER_PARA**: Ação para mover um arquivo.
- **COPIAR_PARA**: Ação para copiar um arquivo.
- **RENOMEAR_PARA**: Ação para renomear um arquivo.
- **EXCLUIR**: Ação para excluir um arquivo. Use com extrema cautela!
- **APLICAR_TAGS**: Ação para adicionar tags ao nome de um arquivo.

---

### Variáveis de Metadados

As variáveis de metadados permitem que você se refira a atributos dos arquivos. Elas são sempre prefixadas com `$`:

- `$NOME`: Nome completo do arquivo (ex: `"documento.pdf"`).
- `$NOME_BASE`: Nome do arquivo sem a extensão (ex: `"documento"`).
- `$EXTENSAO`: Extensão do arquivo (ex: `"pdf"`).
- `$TAMANHO_KB`: Tamanho do arquivo em Kilobytes (número inteiro).
- `$TAMANHO_MB`: Tamanho do arquivo em Megabytes (número inteiro, resultado da divisão por 1024, truncado).
- `$DATA_CRIACAO`: Data de criação do arquivo (string no formato `"YYYY-MM-DD"`).
- `$DATA_MODIFICACAO`: Data da última modificação do arquivo (string no formato `"YYYY-MM-DD"`).
- `$TIPO_MIME`: Tipo MIME do arquivo (ex: `"application/pdf"`, `"image/jpeg"`).

---

### Operadores de Comparação

Usados nas condições para comparar variáveis de metadados com valores:

| Operador              | Descrição                        | Compatível com           |
|-----------------------|----------------------------------|--------------------------|
| **EH**                | É igual a                        | STRING, NUMERO, DATA     |
| **NAO_EH**            | Não é igual a                    | STRING, NUMERO, DATA     |
| **CONTEM**            | Contém a substring (case-sensitive) | STRING               |
| **NAO_CONTEM**        | Não contém a substring           | STRING                   |
| **COMECA_COM**        | Começa com a substring           | STRING                   |
| **TERMINA_COM**       | Termina com a substring          | STRING                   |
| **MAIOR_QUE**         | Estritamente maior que           | NUMERO, DATA             |
| **MENOR_QUE**         | Estritamente menor que           | NUMERO, DATA             |
| **IGUAL_OU_MAIOR_QUE**| Maior ou igual a                 | NUMERO, DATA             |
| **IGUAL_OU_MENOR_QUE**| Menor ou igual a                 | NUMERO, DATA             |

---

### Valores

Os valores usados nas comparações e ações podem ser:

- **STRING**: Texto entre aspas duplas (ex: `"meu_arquivo.txt"`, `"C:/Users/Documentos"`).
- **NUMERO**: Números inteiros ou decimais (ex: `1024`, `5.5`, `-20`).
- **DATA**: Strings no formato `"YYYY-MM-DD"` (ex: `"2024-01-15"`).

---

### Ações

As ações são as operações que o script Bash gerado realizará nos arquivos:

- **MOVER_PARA** `"caminho/destino"`: Move o arquivo. O caminho pode ser absoluto ou relativo à pasta raiz definida.
- **COPIAR_PARA** `"caminho/destino"`: Copia o arquivo.
- **RENOMEAR_PARA** `"novo_nome_com_variaveis.ext"`: Renomeia o arquivo. Você pode usar variáveis de metadados dentro da string, que serão interpoladas no Bash.
    - Exemplo:
        ```fm
        RENOMEAR_PARA "Processado_${DATA_MODIFICACAO}_${NOME_BASE}.${EXTENSAO}"
        ```
- **EXCLUIR**: Deleta o arquivo.
- **APLICAR_TAGS** `"tag1", "tag2"`: Adiciona tags ao início do nome do arquivo no formato `[tag1][tag2]original_nome.ext`.

---

### Comentários

Você pode usar comentários para documentar suas regras:

- **Linha única**: Começa com `//`
- **Bloco**: Começa com `/*` e termina com `*/`

</details>

## Exemplo 

```bash
PASTA_RAIZ "/home/jotavin/Downloads"

// 1. Regra: Organizar PDFs
// PDFs são movidos para a pasta de Documentos e tagueados com "[Downloads]"
REGRA SE $EXTENSAO EH "pdf"
ENTAO MOVER_PARA "/home/jotavin/Documentos"
E RENOMEAR_PARA "[Downloads]${NOME_BASE}.${EXTENSAO}"

// 2. Regra: Organizar Imagens
// Imagens são movidas para a pasta de Imagens e renomeadas com data e tipo MIME
REGRA SE $TIPO_MIME CONTEM "image/"
ENTAO MOVER_PARA "/home/jotavin/Imagens"
E RENOMEAR_PARA "IMG_${DATA_MODIFICACAO}_${NOME_BASE}.${EXTENSAO}"

// 3. Regra: Arquivar Arquivos Antigos da Pasta de Downloads
// Arquivos em Downloads criados antes de 2024-01-01 são movidos para uma pasta "temp" dentro de Downloads
REGRA SE $DATA_CRIACAO MENOR_QUE "2024-01-01"
ENTAO MOVER_PARA "/home/jotavin/Downloads/temp"

// 4. Regra: Tagear Documentos por Tamanho (P, M, G)
// Aplica tags "[P]", "[M]", "[G]" com base no tamanho do arquivo em KB
// P: até 100 KB (Pequeno)
// M: de 101 KB a 1024 KB (Médio)
// G: acima de 1024 KB (Grande)
REGRA SE $EXTENSAO EH "doc" OU $EXTENSAO EH "docx" OU $EXTENSAO EH "odt" OU $EXTENSAO EH "txt" E $TAMANHO_KB IGUAL_OU_MENOR_QUE 100 ENTAO APLICAR_TAGS "P"
REGRA SE $EXTENSAO EH "doc" OU $EXTENSAO EH "docx" OU $EXTENSAO EH "odt" OU $EXTENSAO EH "txt" E $TAMANHO_KB MAIOR_QUE 100 E $TAMANHO_KB IGUAL_OU_MENOR_QUE 1024 ENTAO APLICAR_TAGS "M"
REGRA SE $EXTENSAO EH "doc" OU $EXTENSAO EH "docx" OU $EXTENSAO EH "odt" OU $EXTENSAO EH "txt" E $TAMANHO_KB MAIOR_QUE 1024 ENTAO APLICAR_TAGS "G"

// 5. Regra: Mover Arquivos Compactados para Pasta de Arquivos
// Move arquivos .zip e .rar para uma pasta específica de arquivos compactados
REGRA SE $EXTENSAO EH "zip" OU $EXTENSAO EH "rar"
ENTAO MOVER_PARA "/home/jotavin/ArquivosCompactados"
```

## Contributors

- Antonio Cicero Azevedo - 811455
- João Paulo Migliati - 802534
- João Otávio Langer - 811797