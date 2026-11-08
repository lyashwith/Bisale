import code_input
import lexer
import parser
code=code_input.code_input()
tokens=lexer.lexer(code)
a=parser.parser(tokens)
print(a)
