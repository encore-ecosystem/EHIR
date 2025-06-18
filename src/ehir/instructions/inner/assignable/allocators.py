from dataclasses import dataclass
from ..assignable.assignable import EHIR_Assignable_Instruction
from ....aggregate import EHIR_StructureDefinition
from typing import Union

@dataclass
class EHIR_Instruction_caps(EHIR_Assignable_Instruction):
    structure : EHIR_StructureDefinition

    def __repr__(self) -> str:
        return f"{super().__repr__()} caps {self.structure.declaration.name}"

@dataclass
class EHIR_Instruction_caph(EHIR_Assignable_Instruction):
    structure : EHIR_StructureDefinition

    def __repr__(self) -> str:
        return f"{super().__repr__()} caph {self.structure.declaration.name}"

EHIR_Instruction_MemoryAllocator = Union[EHIR_Instruction_caps, EHIR_Instruction_caph]
