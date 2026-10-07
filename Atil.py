while True:
    try:
        filename = input("Enter Bisale name to cook:")
        with open(f"{filename}.bisale", "r") as file:
            code = file.read()
            break
    except FileNotFoundError as e:
        print(f"{e}")
lines = code.splitlines()
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

def parser(tokens):
    pos=0
    variables={}
    while pos<len(tokens):
        if tokens[pos][0] == "INT":
            if tokens[pos+1][0]=="LEFT_PARENT":
                if tokens[pos+2][0] == "IDENTIFIER":
                    pos2=pos+3
                    if tokens[pos2][0] == "EQUAL":
                        if tokens[pos2+1][0] == "INTEGER":
                            variables[tokens[pos+2][1]] = int(tokens[pos2+1][1])
                            pos2+=2
                        else:
                            variables[tokens[pos+2][1]] = 0
                    else:
                        variables[tokens[pos+2][1]] = 0
                    while tokens[pos2][0]=="COMMA":
                        if tokens[pos2+1][0]=="IDENTIFIER":
                                if tokens[pos2+2][0]=="EQUAL":
                                    if tokens[pos2+3][0]=="INTEGER":
                                        variables[tokens[pos2+1][1]]=int(tokens[pos2+3][1])
                                        pos2+=4
                                else:
                                    variables[tokens[pos2+1][1]] = 0
                                    pos2+=2
                        else:
                            break
                    if tokens[pos2][0] == "RIGHT_PARENT":
                        pass
        elif tokens[pos][0] == "OUTPUT":
            if tokens[pos+1][0] == "LEFT_PARENT":
                if tokens[pos+2][0] == "IDENTIFIER":
                    pos2=pos+3
                    if tokens[pos2][0] == "RIGHT_PARENT":
                        if tokens[pos2+1][0] == "SEMICOLON":
                            print(variables[tokens[pos+2][1]])
                    elif tokens[pos2][0] == "COMMA":
                        print(variables[tokens[pos+2][1]], end="")
                        while tokens[pos2][0] == "COMMA":
                            if tokens[pos2+1][0] == "IDENTIFIER":
                                print(variables[tokens[pos2+1][1]], end="")
                                pos2 += 2
                            else:
                                break
                        if tokens[pos2][0] == "RIGHT_PARENT":
                            if tokens[pos2+1][0] == "SEMICOLON":
                                print()
        pos+=1
    return variables
tokens=lexer(code)
parser(tokens)

