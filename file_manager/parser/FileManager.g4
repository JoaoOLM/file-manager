grammar FileManager;

// --- REGRAS LÉXICAS (TOKENS) ---

// Palavras-Chave
PASTA_RAIZ      : 'PASTA_RAIZ';
REGRA           : 'REGRA';
SE              : 'SE';
E               : 'E';
OU              : 'OU';
ENTAO           : 'ENTAO';
MOVER_PARA      : 'MOVER_PARA';
COPIAR_PARA     : 'COPIAR_PARA';
RENOMEAR_PARA   : 'RENOMEAR_PARA';
EXCLUIR         : 'EXCLUIR';
APLICAR_TAGS    : 'APLICAR_TAGS';

// Operadores de Comparação
EH              : 'EH';
NAO_EH          : 'NAO_EH';
CONTEM          : 'CONTEM';
NAO_CONTEM      : 'NAO_CONTEM';
COMECA_COM      : 'COMECA_COM';
TERMINA_COM     : 'TERMINA_COM';
MAIOR_QUE       : 'MAIOR_QUE';
MENOR_QUE       : 'MENOR_QUE';
IGUAL_OU_MAIOR_QUE : 'IGUAL_OU_MAIOR_QUE';
IGUAL_OU_MENOR_QUE : 'IGUAL_OU_MENOR_QUE';

// Variáveis de Metadados
VAR_NOME            : '$NOME';
VAR_NOME_BASE       : '$NOME_BASE';
VAR_EXTENSAO        : '$EXTENSAO';
VAR_TAMANHO_KB      : '$TAMANHO_KB';
VAR_TAMANHO_MB      : '$TAMANHO_MB';
VAR_DATA_CRIACAO    : '$DATA_CRIACAO';
VAR_DATA_MODIFICACAO: '$DATA_MODIFICACAO';
VAR_TIPO_MIME       : '$TIPO_MIME';

// Literais
STRING          : '"' (~["\r\n\\] | '\\' .)* '"'; // String entre aspas duplas, aceita escapes
NUMERO          : '-'? DIGITO+ ('.' DIGITO+)?; // Números inteiros ou decimais, opcionalmente negativos
DIRETORIO       : '/' (~[\r\n\t ]+)+; // Caminho de diretório iniciado por /, não contém espaço
ID              : (LETRA | '_') (LETRA | DIGITO | '_')*; // Identificadores genéricos, se precisar

// Espaços em branco e comentários (serão ignorados pelo lexer)
WS              : [ \t\r\n]+ -> skip;
COMENTARIO_LINHA: '//' ~[\r\n]* -> skip;
COMENTARIO_BLOCO: '/*' .*? '*/' -> skip;

// Fragmentos (usados para construir tokens maiores, não são tokens por si só)
fragment DIGITO : [0-9];
fragment LETRA  : [a-zA-Z];

// --- REGRAS SINTÁTICAS (PARSER) ---

// Regra inicial do programa
programa        : declaracaoPastaRaiz (regra)* EOF;

// Declaração da pasta raiz
declaracaoPastaRaiz : PASTA_RAIZ STRING; // O caminho da pasta raiz deve ser uma STRING

// Definição de uma regra
regra           : REGRA SE condicao ENTAO acao (E acao)*;

// Condições (lógicas combinadas)
condicao        : expressaoBooleana ( (E | OU) expressaoBooleana )*;

// Expressão booleana simples
expressaoBooleana : variavelMetadata operadorComparacao valor;

// Variáveis de metadados
variavelMetadata : VAR_NOME
                 | VAR_NOME_BASE
                 | VAR_EXTENSAO
                 | VAR_TAMANHO_KB
                 | VAR_TAMANHO_MB
                 | VAR_DATA_CRIACAO
                 | VAR_DATA_MODIFICACAO
                 | VAR_TIPO_MIME;

// Operadores de comparação
operadorComparacao : EH
                   | NAO_EH
                   | CONTEM
                   | NAO_CONTEM
                   | COMECA_COM
                   | TERMINA_COM
                   | MAIOR_QUE
                   | MENOR_QUE
                   | IGUAL_OU_MAIOR_QUE
                   | IGUAL_OU_MENOR_QUE;

// Valor que será comparado (string ou número)
valor           : STRING | NUMERO;

// Ações
acao            : moverPara
                | copiarPara
                | renomearPara
                | excluir
                | aplicarTags;

// Ações específicas
moverPara       : MOVER_PARA STRING;
copiarPara      : COPIAR_PARA STRING;
renomearPara    : RENOMEAR_PARA stringComVariaveis;
excluir         : EXCLUIR;
aplicarTags     : APLICAR_TAGS listaTags;

// Lista de tags (ex: "tag1", "tag2")
listaTags       : STRING (',' STRING)*;

// String que pode conter variáveis (para RENOMEAR_PARA)
// Esta regra é mais complexa e permite misturar texto literal e variáveis.
// O ANTLR não permite interpolação de strings diretamente, então você terá que processar isso na análise semântica.
// Aqui, definimos que é uma string que pode ter os placeholders das variáveis.
// Ex: "Meu_Arquivo_${DATA_MODIFICACAO}.txt"
// O lexer vai pegar "Meu_Arquivo_", "$", "DATA_MODIFICACAO", ".txt" separadamente.
// No parser, vamos tentar agrupar isso.
// Uma abordagem mais simples para o parser é tratar isso como um STRING completo e fazer a interpolação na fase semântica.
// Ou podemos ser mais explícitos:
stringComVariaveis : (STRING_PARTE | VARIAVEL_INTERPOLADA)+;

// STRING_PARTE pega qualquer texto literal que não seja uma variável de metadado
// Cuidado: Esta é uma regra léxica auxiliar, e pode entrar em conflito se for muito genérica.
// A abordagem mais robusta é ter um token STRING e na análise semântica, você procura por padrões ${VAR} dentro dela.
// Para fins da gramática, vamos manter STRING, e você lida com a interpolação posteriormente.
// Vamos ajustar 'renomearPara' para usar STRING e deixar a lógica de variáveis para a fase semântica.
// A interpolação de variáveis em strings é geralmente tratada na fase de interpretação/geração de código, não diretamente no parser.
// O ANTLR simplesmente reconhecerá isso como uma STRING.

// Revisitando: Para simplificar no ANTLR, a string de renomeação será uma STRING normal,
// e você fará a substituição das variáveis (`$NOME`, etc.) nela durante a fase semântica/interpretação.
// Então, a regra `stringComVariaveis` será substituída por `STRING`.
// Isso é uma simplificação que faz sentido para o ANTLR.

// Reajustando a regra de renomearPara:
// renomearPara : RENOMEAR_PARA STRING; // Onde STRING pode conter as variáveis como "$NOME_BASE"