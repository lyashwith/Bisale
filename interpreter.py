filename = input("Enter Bisale file: ")
with open(f"{filename}.bisale", "r") as file:
    code = file.read()
lines = code.splitlines()
variables={}
for line in lines:
    if line.startswith("int("):
        content = line[4:-1]
        variable,value=content.split("=")
        value=int(value)
        variables[variable]=value
    elif line.startswith("tojpav("):
        content = line[7:-2]
        values = content.split(",")
        for value in values:
            value = value.strip()
            if len(values) > 1:
                print(variables[value], end=" ")
            else:
                print(variables[value])
