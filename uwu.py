import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__)) # I really hate that I have to do this lmfao

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
                    # Code for variables
                    elif command.startswith(">") and command.endswith("<") and "//" in command:
                        # Is this needlessly complicated? Probably. I'll change it some other time. Or YOU can! :3
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
                        print("ERROR! Unknown command: ", command)
                        sys.exit()
                else:
                    pass

with open(os.path.join(root_dir, "program.uwu"), "r") as file: # TODO: Add the ability to provide a file path (or make it required)
    interpret(file.read())