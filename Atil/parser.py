from AST_nodes import VariableDeclaration, MultiDeclaration
class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    def current(self):
        return self.tokens[self.pos]
    def advance(self):
        token = self.current()
        self.pos += 1
        return token
    def expect(self, token_type):
        if self.current()[0] == token_type:
            return self.advance()
        else:
            raise SyntaxError(f"Expected {token_type},You have written {self.current()[0]}")
    def parse_int_declaration(self):
        self.expect("INT")
        self.expect("LEFT_PARENT")
        variables = []
        name = self.expect("IDENTIFIER")[1]
        if self.current()[0] == "EQUAL":
            self.advance()
            value = int(self.expect("INTEGER")[1])
        else:
            value = 0
        variables.append(VariableDeclaration(name, value))
        self.expect("RIGHT_PARENT")
        return MultiDeclaration(variables)
