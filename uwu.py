import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir.startswith("/tmp"): 
    root_dir = "."

def interpret(code):
    char = 0
    message = ""
    inputmode = False
    comment = False
    vars = {}
    for line in code.split("\n"):
        for command in line.split(" "):
            command = str(command)
            if command == "o3o":
                comment = not comment
            else:
                if not comment:
                    if command == "uwu":
                        char += 1
                    elif command == "UWU":
                        char += 10
                    elif command == "owo":
                        char += 5
                    elif command == "OWO":
                        char += 50
                    elif command == "nya":
                        message += chr(char)
                        char = 0
                    elif command == ">:3":
                        print(message, end="")
                        message = "" 
                    elif command == ":3c":
                        inputmode = True
                    elif command.startswith(">") and command.endswith("<") and "//" in command:
                        varname = f"var{str(len(''.join(char for char in command if char == '/')) - 1)}"
                        if inputmode:
                            vars[varname] = input()
                            try:
                                vars[varname] = int(vars[varname])
                            except Exception:
                                pass
                            inputmode = False
                        else:
                            message += str(vars[varname])
                        varname = "NIL"
                    elif command == "" or command == None or command == " ":
                        pass
                    else:
                        print("Unknown command:", command)
                        sys.exit()
                else:
                    pass

with open(os.path.join(root_dir, "program.uwu"), "r") as file:
    interpret(file.read())