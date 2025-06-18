from dataclasses import dataclass
from .block import EHIR_InstructionsBlock
from ..aggregate import EHIR_StructureDeclaration, EHIR_Pointer
from ..instructions.inner.unassignable.control_flow import EHIR_Instruction_br
from ..instructions.inner.assignable.allocators import EHIR_Instruction_caph

@dataclass
class EHIR_FunctionDeclaration:
    is_public : bool
    name      : str
    params    : list[EHIR_Pointer]
    ret_type  : EHIR_StructureDeclaration

    def __repr__(self) -> str:
        params = ", ".join([p.__repr__() for p in self.params])
        return f"fn {'@' if self.is_public else '%'}{self.name}({params}) -> {self.ret_type}"


@dataclass
class EHIR_FunctionImplementation:
    declaration : EHIR_FunctionDeclaration
    allocations : list[EHIR_Instruction_caph | EHIR_Instruction_br]
    body        : dict[str, EHIR_InstructionsBlock]

    def new_block(self, block_name: str = "bb") -> EHIR_InstructionsBlock:
        new_block_name = block_name
        i = 0
        while True:
            if new_block_name not in self.body:
                res = EHIR_InstructionsBlock(name=new_block_name, body=[])
                self.body[new_block_name] = res
                return res
            new_block_name = f"{new_block_name}.{i}"
            i += 1

    @classmethod
    def default_entry_block_name(self) -> str:
        return "entry"
    
    def __repr__(self) -> str:
        definition = f"impl {self.declaration.name}"
        definition += " {\n"

        # Allocations
        if len(self.allocations) > 0:
            definition += "allocations:\n"
            for instruction in self.allocations:
                definition += "\t" + instruction.__repr__() + "\n"

        # Body
        for block_name, block in self.body.items():
            definition += f"{block_name}:\n"
            for instruction in block.body:
                definition += "\t" + instruction.__repr__() + "\n"
        definition += "}"
        return definition
