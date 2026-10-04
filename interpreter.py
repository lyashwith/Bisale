while True:
    try:
        filename = input("Enter Bisale name to cook: ")
        with open(f"{filename}.bisale", "r") as file:
            code = file.read()
            break
    except FileNotFoundError as e:
        print(f"{e}")
lines = code.splitlines()
variables={}

def lexer(code):
    code_word=""
    for character in code:
        if code_word=="\n":
            code_word=""
        else:
            code_word=code_word+character
        print(code_word)
lexer(code)

for line in lines:
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
                    print(variable)
