from dataclasses import dataclass
from .assignable import EHIR_Assignable_Instruction
from ....aggregate import EHIR_Pointer
from abc import ABCMeta

@dataclass
class EHIR_Instruction_Binop(EHIR_Assignable_Instruction, metaclass=ABCMeta):  # noqa: N801
    op  : str
    lhs : EHIR_Pointer
    rhs : EHIR_Pointer

    def __repr__(self) -> str:
        return f"{super().__repr__()} {self.op} {self.lhs}, {self.rhs}"

@dataclass
class EHIR_Instruction_add(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_sub(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_mul(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_div(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_ieq(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_neq(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_grt(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_geq(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_les(EHIR_Instruction_Binop):
    pass

@dataclass
class EHIR_Instruction_leq(EHIR_Instruction_Binop):
    pass
