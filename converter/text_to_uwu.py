import os
from pathlib import Path

root_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute().__str__()

def convert(text):
    newtext = ""
    uni = 0
    for char in text:
        uni = ord(char)
        while uni > 0:
            if uni > 50:
                newtext += "OWO "
                uni -= 50
            elif uni > 10:
                newtext += "UWU "
                uni -= 10
            elif uni > 5:
                newtext += "owo "
                uni -= 5
            elif uni >= 1:
                newtext += "uwu "
                uni -= 1
        newtext += "nya\n"
    newtext += "UWU nya\n>:3"
    return newtext

with open(os.path.join(root_dir, "converter/in.txt"), "r") as inp:
    program = convert(inp.read())
    with open(os.path.join(root_dir, "converter/in.txt"), "w") as out:
        out.write(program)