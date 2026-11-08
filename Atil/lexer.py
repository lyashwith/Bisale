
def lexer(code):
    tokens=[]
    for line in code.split("\n"):
        code_word=""
        space_seen=False
        bad=False
        for character in line:
            if character in " \t":
                if code_word!="":
                    space_seen=True
            elif character == "(":
                if code_word=="int":
                    tokens.append(("INT",code_word))
                elif code_word == "thojpav":
                    tokens.append(("OUTPUT", code_word))
                else:
                    bad=True
                    break
                tokens.append(("LEFT_PARENT",character))
                code_word = ""
            elif character=="=":
                if code_word!="":
                    tokens.append(("IDENTIFIER",code_word))
                else:
                    bad=True
                    break
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
                if code_word!="":
                    bad=True
                    break
                tokens.append(("SEMICOLON", character))
            else:
                if code_word=="":
                    space_seen=False
                if space_seen:
                    bad=True
                    break
                code_word+=character

        if code_word!="":
            bad=True
        if bad:
            tokens.append(("UNKNOWN", line))
            return tokens

    return tokens
