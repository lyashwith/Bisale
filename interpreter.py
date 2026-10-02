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
for line in lines:
    if line.startswith("int("):
        content = line[4:-1]
        variable,value=content.split("=")
        value=int(value)
        variables[variable]=value
    if line.endswith(";"):
        if line.startswith("thojpav("):
            content = line[8:-2]
            values = content.split(",")
            for value in values:
                value = value.strip()
                if len(values) > 1:
                    print(variables[value], end=" ")
                else:
                    print(variables[value])
