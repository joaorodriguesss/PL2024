import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'INPUT',
    'OUTPUT',
    'ASSIGN',  # Novo token para atribuição
)

# Regras de expressão regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INPUT = r'\?'
t_OUTPUT = r'!'
t_ASSIGN = r'='  # Regra para atribuição

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define uma regra para identificar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro para caracteres inválidos
def t_error(t):
    print("Caracter inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Regras da gramática
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Gramática
def p_statement_input(p):
    'statement : INPUT expression'
    print("Input:", p[2])

def p_statement_output(p):
    'statement : OUTPUT expression'
    print("Output:", p[2])

def p_statement_assignment(p):
    'statement : IDENTIFIER ASSIGN expression'
    print("Atribuição:", p[1], "=", p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe!")

# Construção do parser
parser = yacc.yacc(method='SLR')

# Função para interpretação
def interpret(text):
    lines = text.strip().split('\n')
    for line in lines:
        result = parser.parse(line, lexer=lexer)

# Exemplo de uso
if __name__ == "__main__":
    text = """
    ?a
    b = a * 2/ (27-3)
    !a+b
    c = a*b / (a/b)
    """
    interpret(text)
