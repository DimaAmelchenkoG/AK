import sys

from isa import Term, Opcode
import json

labels = {}
vars = {}
code = []

def getVars(source):
    index_of_data = source.index('.data')
    index_of_code = source.index('.code')
    for i in range(index_of_data+1, index_of_code):
        var = source[i].split(" ", 1)
        var[0] = var[0][:-1]
        #print(var[0], var[1])
        if var[1].startswith("\""):
            vars[var[0]] = {"value": var[1], "number": len(vars)}
        elif not(var[1].isdigit()):
            print("var", var)
            vars[var[0]] = {"value": var[1], "number": len(vars)}
        else:
            var[1] = int(var[1])
            vars[var[0]] = {"value": var[1], "number": len(vars)}


def getLabels(source):
    number_of_line = 0
    for i in range(len(source)):
        if source[i].endswith(":"):
            labels[source[i][:-1]] = number_of_line
        elif not(source[i].startswith(".")):
            number_of_line += 1


def getCode(source):
    index_of_command = 0

    for var in vars.items():
        js = {"index": index_of_command, "opcode": Opcode("var").value, "arg": var[1]["value"], "name": var[0]}
        code.append(js)
        index_of_command += 1

    index_of_code = source.index('.code')
    for i in range(index_of_code+1, len(source)):
        if not(source[i].endswith(":")):
            if len(source[i].split()) > 1 and source[i].split()[1] in vars:
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value, "arg": vars[source[i].split()[1]]["number"]}
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1][1:] in vars:
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value, "arg": vars[source[i].split()[1][1:]]["number"], "kosven": 1}
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1] in labels:
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value, "arg": labels[source[i].split()[1]]}
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1].isdigit():
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value, "arg": "$" + source[i].split()[1]}
                index_of_command += 1
                code.append(js)
            elif len(source[i].split()) > 1 and source[i].split()[1] in ["out", "in"]:
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value, "arg": source[i].split()[1]}
                index_of_command += 1
                code.append(js)
            else:
                #print(source[i])
                js = {"index": index_of_command, "opcode": Opcode(source[i].split()[0]).value}
                index_of_command += 1
                code.append(js)

def translate(source):
    code.clear()
    for i in range(len(source)):
        if source[i].endswith("\n"):
            source[i] = source[i][:-1]
        source[i] = source[i].split(";")[0].strip()
    #print(source)
    #print("--------")
    getVars(source)
    getLabels(source)
    #print('vars', vars)
    #print(labels)
    getCode(source)

    #for a in code:
        #print(a)

    return code




def main(source, target):
    code = []

    labels.clear()
    vars.clear()
    code.clear()

    #source = open(source).readlines()
    with open(source, encoding="utf-8") as f:
        source = f.readlines()

    source = [x for x in source if x != "\n"]
    code = translate(source)

    #for a in code:
       # print(a)


    with open(target, 'w') as f:
        f.write(json.dumps(code))

    print("source LoC:", len(source), "code instr:", len(code))

if __name__ == "__main__":
    #source = 'cat_1_asm.txt'
   # target = 'target_file.json'
   # main(source, target)

    _, source, target = sys.argv
    main(source, target)