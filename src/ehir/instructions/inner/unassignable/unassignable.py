from dataclasses import dataclass
from ...instruction import EHIR_Instruction
from ....aggregate import EHIR_Pointer, EHIR_StructureInitialization

@dataclass
class EHIR_Unassignable_Instruction(EHIR_Instruction):
    pass

@dataclass
class EHIR_Instruction_store(EHIR_Unassignable_Instruction):
    store_in       : EHIR_Pointer
    initialization : EHIR_StructureInitialization
    
    def __repr__(self) -> str:
        return f"store {self.store_in}, {self.initialization}"
