import ply.lex as lex

# Lexer tokens
tokens = (
    'STRING',
    'PRINTLN',
    'SHOW',
    'LABEL',
    'TITLE',
    'RELATIVE',
    'SIZE',
    'INTEGER',
    'EVAL',
    'BTN',
    'MSGBOX',
    'CHECKBOX',
    'INPUTFIELD'
)

# Lexer rules
t_STRING = r'"[^"]*"'
t_INTEGER = r'\d+'
t_PRINTLN = r'println'
t_SHOW = r'show'
t_RELATIVE = r'import'
t_LABEL = r'label'
t_TITLE = r'title'
t_SIZE = r'size'
t_EVAL = r'eval'
t_BTN = r'pushbutton'
t_MSGBOX = r'messagebox'
t_CHECKBOX = r'checkbox'
t_INPUTFIELD = r'inputfield'

# Ignored characters
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Unexpected character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
