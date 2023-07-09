import ply.yacc as yacc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from lexer.lexer import tokens, lexer
import importlib

# Global variables
window = None
app = QApplication([])
window = QWidget()

# Parser rules
def p_program(p):
    '''program : statement
               | program statement'''

def p_statement_println(p):
    'statement : PRINTLN STRING'
    print(p[2][1:-1])

def p_statement_setsize(p):
    'statement : SIZE INTEGER INTEGER'
    window.resize(int(p[2]), int(p[3]))

def p_statement_create(p):
    'statement : SHOW'
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec())

def p_statement_relative(p):
    'statement : RELATIVE STRING'
    importlib.import_module(p[2][1:-1])

def p_statement_label(p):
    'statement : LABEL STRING INTEGER INTEGER'
    QLabel(p[2][1:-1], parent=window).move(int(p[3]), int(p[4]))

def p_error(p):
    print("Syntax error")

def p_statement_title(p):
    'statement : TITLE STRING'
    window.setWindowTitle(p[2][1:-1])

def p_statement_eval(p):
    'statement : EVAL STRING'
    eval(p[2][1:-1])

def p_statement_btn(p):
    'statement : BTN STRING INTEGER INTEGER'
    QPushButton(p[2][1:-1], parent=window).move(int(p[3]), int(p[4]))

def p_statement_msgbox(p):
    'statement : MSGBOX STRING STRING STRING STRING'
    QMessageBox.question(window, p[2][1:-1], p[3][1:-1],  QMessageBox.Yes if p[4][1:-1] == "yes" else QMessageBox.No, QMessageBox.Yes if p[4][1:-1] == "yes" else QMessageBox.No)

def p_statement_checkbox(p):
    'statement : CHECKBOX STRING INTEGER INTEGER'
    box = QCheckBox(p[2][1:-1], window)
    box.move(int(p[3]), int(p[4]))
    
def p_statement_inputfield(p):
    'statement : INPUTFIELD INTEGER INTEGER'
    QLineEdit(window).move(int(p[2]), int(p[3]))

parser = yacc.yacc(outputdir="cache/", debug=False)

with open(sys.argv[1], "r") as file:
    code = file.read()

lexer.input(code)
parser.parse(code)