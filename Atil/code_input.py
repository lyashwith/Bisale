def code_input():
    while True:
        try:
            filename = input("Enter Bisale name to cook:")
            with open(f"{filename}.bisale", "r") as file:
                code = file.read()
                break
        except FileNotFoundError as e:
            print(f"{e}")
    return code
