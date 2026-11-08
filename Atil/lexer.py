
variables={}

def lexer(code):
    tokens=[]
    code_word=""
    for character in code:
        if character=="\n":
            code_word=""
        elif character == "(":
            if code_word=="int":
                tokens.append(("INT",code_word))
            elif code_word == "thojpav":
                tokens.append(("OUTPUT", code_word))
            tokens.append(("LEFT_PARENT",character))
            code_word = ""
        elif character=="=":
            if code_word!="":
                tokens.append(("IDENTIFIER",code_word))
            tokens.append(("EQUAL",character))
            code_word=""
        elif character == ",":
            if code_word.isdigit():
                tokens.append(("INTEGER", code_word))
            elif code_word != "":
                tokens.append(("IDENTIFIER", code_word))
            tokens.append(("COMMA", character))
            code_word = ""
        elif character == ")":
            if code_word.isdigit():
                tokens.append(("INTEGER",code_word))
            elif code_word != "":
                tokens.append(("IDENTIFIER",code_word))
            tokens.append(("RIGHT_PARENT",character))
            code_word = ""
        elif character == ";":
            tokens.append(("SEMICOLON", character))
        elif character in " \t":
            pass
        else:
            code_word=code_word+character
    
    return tokens