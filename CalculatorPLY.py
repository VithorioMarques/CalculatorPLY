import ply.lex as lex
import ply.yacc as yacc

########################################## Scanner ##########################################

tokens = (
   'SUM',
   'SUBTRACT',
   'DIVIDE',
   'MULTIPLY',
   'NUM',
   'ID',
   'LPAREN',
   'RPAREN',
)

# Regex to define tokens

#t_OP_ARIT = "\+ | - | \* | /"  --> had to split in diferent tokens to be able to setup MULTIPLY and DIVIDE precedence over SUM and SUBTRACT

t_SUM      = '\+'
t_SUBTRACT = '-'
t_DIVIDE   = '/'
t_MULTIPLY = '\*'

def t_NUM(t):
     #"(([0-9]+\.[0-9]+) | [0-9]+)"
     "-?[0-9]+(\.[0-9]+)?"
     t.value = float(t.value)
     return t

t_ID      = "[a-zA-Z][a-z|A-Z|0-9]*"
t_LPAREN  = "\("
t_RPAREN  = "\)"
t_ignore  = " \t\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

#############################################################################################

########################################## Parsing ##########################################

precedence = (
    ('left','SUM', 'SUBTRACT'),
    ('left','DIVIDE', 'MULTIPLY'),
    )

def p_expressao(p):
    '''expressao : expressao SUM expressao
                  | expressao SUBTRACT expressao
                  | expressao DIVIDE expressao
                  | expressao MULTIPLY expressao
                  | NUM
                  | ID
                  | LPAREN expressao RPAREN'''
    if len(p) == 4: 
         if   p[2] == '+': p[0] = p[1] + p[3]
         elif p[2] == '-': p[0] = p[1] - p[3]
         elif p[2] == '*': p[0] = p[1] * p[3]
         elif p[2] == '/': p[0] = p[1] / p[3]
         else: p[0] = p[2]
    else:
         p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")
#############################################################################################

parser = yacc.yacc()

while True:
   try:
       print("Insert the expression: ")
       s = input("calc >")
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)