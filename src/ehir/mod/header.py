from dataclasses import dataclass
from ..instructions import (
    EHIR_Instruction_imp,
    EHIR_Instruction_structure_delcaration,
    EHIR_Instruction_strucure_definition,
    EHIR_Instruction_function_declaration,
)

@dataclass
class EHIR_Header:
    imports         : list[EHIR_Instruction_imp]
    structure_decls : dict[str, EHIR_Instruction_structure_delcaration]
    structure_defs  : dict[str, EHIR_Instruction_strucure_definition]
    function_decls  : dict[str, EHIR_Instruction_function_declaration]
    
    @classmethod
    def default(cls) -> "EHIR_Header":
        return EHIR_Header(
            imports           = [],
            structure_decls   = {},
            structure_defs    = {},
            function_decls    = {},
        )


__all__ = [
    "EHIR_Header",
]
