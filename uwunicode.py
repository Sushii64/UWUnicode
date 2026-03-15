import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__)) # I really hate that I have to do this lmfao

def interpret(code):
    char = 0
    register = ""
    mode = "normal"
    comment = False
    vars = {}
    tempmath = {"var1": 0, "var2": 0}
    for line in code.split("\n"):
        for command in line.split(" "):
            # print(command, vars)
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
                        register += chr(char)
                        char = 0
                    elif command == ">:3":
                        print(register, end="")
                        register = ""
                    elif command == ":3c":
                        mode = "input"
                    elif command == "prr":
                        mode = "set2register"
                    elif command == "mrr":
                        mode = "set2counter"
                    elif command == "^w^":
                        mode = "inc"
                    elif command == "umu":
                        mode = "dec"
                    elif command == "+w+":
                        mode = "addition1"
                    elif command == "-w-":
                        mode = "subtraction1"
                    elif command == "*w*":
                        mode = "multiplication1"
                    elif command == "/w\\":
                        mode = "division1"
                    elif command == "@w@":
                        register = register[:-1]
                    # Code for variables
                    elif command.startswith(">") and command.endswith("<") and "//" in command:
                        # Is this needlessly complicated? Probably. I'll change it some other time. Or YOU can! :3
                        varname = f"var{str(len(''.join(char for char in command if char == '/')) - 1)}"
                        if mode == "input":
                            vars[varname] = input()
                            try:
                                vars[varname] = int(vars[varname])
                            except ValueError:
                                pass
                            mode = "normal"
                        elif mode == "set2register":
                            vars[varname] = register
                            try:
                                vars[varname] = int(vars[varname])
                            except ValueError:
                                pass
                            register = ""
                            mode = "normal"
                        elif mode == "set2counter":
                            vars[varname] = char
                            try:
                                vars[varname] = int(vars[varname])
                            except ValueError:
                                pass
                            char = 0
                            mode = "normal"
                        elif mode == "inc":
                            vars[varname] += 1
                            mode = "normal"
                        elif mode == "dec":
                            vars[varname] -= 1
                            mode = "normal"
                        # This might be the shitties code I've ever written I'm so sorry
                        # TODO: Fix this.
                        elif mode == "addition1":
                            tempmath["var1"] = vars[varname]
                            mode = "addition2"
                        elif mode == "addition2":
                            tempmath["var2"] = vars[varname]
                            char = tempmath["var1"] + tempmath["var2"]
                            tempmath["var1"] = 0
                            tempmath["var2"] = 0
                            mode = "normal"
                        elif mode == "subtraction1":
                            tempmath["var1"] = vars[varname]
                            mode = "subtraction2"
                        elif mode == "subtraction2":
                            tempmath["var2"] = vars[varname]
                            char = tempmath["var1"] - tempmath["var2"]
                            tempmath["var1"] = 0
                            tempmath["var2"] = 0
                            mode = "normal"
                        elif mode == "multiplication1":
                            tempmath["var1"] = vars[varname]
                            mode = "multiplication2"
                        elif mode == "multiplication2":
                            tempmath["var2"] = vars[varname]
                            char = tempmath["var1"] * tempmath["var2"]
                            tempmath["var1"] = 0
                            tempmath["var2"] = 0
                            mode = "normal"
                        elif mode == "division1":
                            tempmath["var1"] = vars[varname]
                            mode = "division2"
                        elif mode == "division2":
                            tempmath["var2"] = vars[varname]
                            char = tempmath["var1"] / tempmath["var2"]
                            tempmath["var1"] = 0
                            tempmath["var2"] = 0
                            mode = "normal"
                        else:
                            register += str(vars[varname])
                        varname = "NIL"
                    elif command == "" or command is None or command == " ":
                        pass
                    else:
                        print("error! unknown command: ", command)
                        sys.exit()
                else:
                    pass


program = os.path.join(root_dir, "program.uwu")
if len(sys.argv) >= 2:
    program = sys.argv[1]

try:
    with open(program, "r") as file:
        # print("running " + program)
        interpret(file.read())
except FileNotFoundError as e:
    print("error! file not found: " + program)