from enum import Enum
from collections import namedtuple
class Opcode(str, Enum):
    VAR = "var"
    LOAD = "ld"
    PRINT = "print"
    READ = "read"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    ST = "st"
    JNZ = "jnz"
    JZ = "jz"
    JMP = "jmp"
    INC = "inc"
    HALT = "halt"
    MOD = "mod"

    def __str__(self):
        """Переопределение стандартного поведения `__str__` для `Enum`: вместо
        `Opcode.INC` вернуть `increment`.
        """
        return str(self.value)

class Term(namedtuple("Term", "line pos symbol")):
    ""