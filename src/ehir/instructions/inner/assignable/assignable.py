from dataclasses import dataclass
from ...instruction import EHIR_InnerInstruction
from ....aggregate import EHIR_Pointer, EHIR_StructureInitialization

@dataclass
class EHIR_Assignable_Instruction(EHIR_InnerInstruction):
    assign_to : EHIR_Pointer

    def __repr__(self) -> str:
        return f"{self.assign_to} ="

@dataclass
class EHIR_Instruction_call(EHIR_Assignable_Instruction):
    func_name : str
    arguments : list[EHIR_Pointer]

    def __repr__(self) -> str:
        return f"{super().__repr__()} call {self.func_name}({', '.join(x.__repr__() for x in self.arguments)})"

@dataclass
class EHIR_Instruction_cast(EHIR_Assignable_Instruction):
    target      : EHIR_Pointer
    target_type : str
    
    def __repr__(self) -> str:
        return f"{super().__repr__()} cast {self.target}, {self.target_type}"

@dataclass
class EHIR_Instruction_getf(EHIR_Assignable_Instruction):
    source  : EHIR_Pointer
    element : EHIR_Pointer
    
    def __repr__(self) -> str:
        return f"{super().__repr__()} getf {self.source}, {self.element}"

