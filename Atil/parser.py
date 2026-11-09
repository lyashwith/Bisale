class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1

    def expect(self, token_type):
        if self.current()[0] == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected {token_type},You have written {self.current()[0]}")
