from dataclasses import dataclass
from ....instructions import EHIR_Unassignable_Instruction
from ....aggregate import EHIR_Pointer


@dataclass
class EHIR_ControlFlow(EHIR_Unassignable_Instruction):
    pass

@dataclass
class EHIR_Instruction_ret(EHIR_ControlFlow):
    value: EHIR_Pointer

    def __repr__(self) -> str:
        return f"ret {self.value}"

@dataclass
class EHIR_Instruction_br(EHIR_ControlFlow):
    destination: str

    def __repr__(self) -> str:
        return f"br {self.destination}"

@dataclass
class EHIR_Instruction_cbr(EHIR_ControlFlow):
    condition : EHIR_Pointer
    true_br   : str
    else_br   : str

    def __repr__(self) -> str:
        return f"cbr {self.condition}, {self.true_br}, {self.else_br}"
