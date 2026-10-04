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
            if code_word != "":
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
    while pos<len(tokens):
        if tokens[pos][0] == "INT":
            if tokens[pos+1][0]=="LEFT_PARENT":
                if tokens[pos+2][0] == "IDENTIFIER":
                    pos2=pos+3
                    while tokens[pos2][0]=="COMMA":
                        if tokens[pos2+1][0]=="IDENTIFIER":
                            print("hi")
                            pos2+=2
                        else:
                            break
                    if tokens[pos2][0] == "RIGHT_PARENT":
                        print("Valid declaration")
        pos+=1

tokens=lexer(code)
parser(tokens)

"""for line in lines:
    if line.startswith("int(") and line.endswith(")"):
        content = line[4:-1]
        if "=" in line:
            variable,value=content.split("=")
            value=int(value)
            variables[variable]=value
            variable=eval(variable,{},variables)
        else:
            variable=content
            value=0
            variables[variable]=value
            variable=eval(variable,{},variables)
    if line.endswith(";"):
        if line.startswith("thojpav("):
            content = line[8:-2]
            values = content.split(",")
            for value in values:
                value = value.strip()
                if len(values) > 1:
                    print(variable, end=" ")
                else:
                    print(variable)"""
