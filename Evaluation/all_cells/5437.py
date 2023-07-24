# JSON output syntax highlighting
from __future__ import print_function
from pygments import highlight
from pygments.lexers import JsonLexer, TextLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

def json_print(inpt):
    string = str(inpt)
    formatter = HtmlFormatter()
    if string[0] == '{':
        lexer = JsonLexer()
    else:
        lexer = TextLexer()
    return HTML('<style type="text/css">{}</style>{}'.format(
                formatter.get_style_defs('.highlight'),
                highlight(string, lexer, formatter)))

globals()['print'] = json_print