import json
import sys

from isa import Opcode

labels = {}
my_vars = {}
code = []


def get_my_vars(source):
    index_of_data = source.index(".data")
    index_of_code = source.index(".code")
    for i in range(index_of_data + 1, index_of_code):
        var = source[i].split(" ", 1)
        var[0] = var[0][:-1]
        if var[1].startswith('"'):
            my_vars[var[0]] = {"value": var[1], "number": len(my_vars)}
        elif not (var[1].isdigit()):
            print("var", var)
            my_vars[var[0]] = {"value": var[1], "number": len(my_vars)}
        else:
            var[1] = int(var[1])
            my_vars[var[0]] = {"value": var[1], "number": len(my_vars)}


def get_labels(source):
    number_of_line = 0
    for i in range(len(source)):
        if source[i].endswith(":"):
            labels[source[i][:-1]] = number_of_line
        elif not (source[i].startswith(".")):
            number_of_line += 1


def get_code(source):
    index_of_command = 0

    for var in my_vars.items():
        js = {"index": index_of_command, "opcode": Opcode("var").value, "arg": var[1]["value"], "name": var[0]}
        code.append(js)
        index_of_command += 1

    index_of_code = source.index(".code")
    for i in range(index_of_code + 1, len(source)):
        if not (source[i].endswith(":")):
            if len(source[i].split()) > 1 and source[i].split()[1] in my_vars:
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": my_vars[source[i].split()[1]]["number"],
                }
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1][1:] in my_vars:
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": my_vars[source[i].split()[1][1:]]["number"],
                    "kosven": 1,
                }
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1] in labels:
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": labels[source[i].split()[1]],
                }
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1].isdigit():
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": "$" + source[i].split()[1],
                }
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1] in ["out", "in"]:
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": source[i].split()[1],
                }
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1].startswith("*"):
                js = {
                    "index": index_of_command,
                    "opcode": Opcode(source[i].split()[0]).value,
                    "arg": source[i].split()[1],
                }
                index_of_command += 1
                code.append(js)
            else:
                """ print(source[i]) """
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value}
                index_of_command += 1
                code.append(js)


def translate(source):
    code.clear()
    for i in range(len(source)):
        if source[i].endswith("\n"):
            source[i] = source[i][:-1]
        source[i] = source[i].split(";")[0].strip()
    get_my_vars(source)
    get_labels(source)
    get_code(source)

    return code


def main(source, target):
    code = []

    labels.clear()
    my_vars.clear()
    code.clear()

    """ source = open(source).readlines()"""
    with open(source, encoding="utf-8") as f:
        source = f.readlines()

    source = [x for x in source if x != "\n"]
    code = translate(source)


    with open(target, "w", encoding="utf-8") as file:
        buf = []
        for instr in code:
            buf.append(json.dumps(instr))
        file.write("[" + ",\n ".join(buf) + "]")



    print("source LoC:", len(source), "code instr:", len(code))


if __name__ == "__main__":
    _, source, target = sys.argv
    main(source, target)
