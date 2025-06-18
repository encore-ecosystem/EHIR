from .instruction import EHIR_Instruction, EHIR_TopLevelInstruction, EHIR_InnerInstruction


from .inner.assignable.assignable import (
    EHIR_Assignable_Instruction,
    
    EHIR_Instruction_call,
    EHIR_Instruction_cast,
    EHIR_Instruction_getf
)

from .inner.assignable.binop import (
    EHIR_Instruction_Binop,
    
    EHIR_Instruction_add,
    EHIR_Instruction_sub,
    EHIR_Instruction_mul,
    EHIR_Instruction_div,
    EHIR_Instruction_ieq,
    EHIR_Instruction_neq,
    EHIR_Instruction_grt,
    EHIR_Instruction_geq,
    EHIR_Instruction_les,
    EHIR_Instruction_leq,
)

from .inner.assignable.allocators import (
    EHIR_Instruction_MemoryAllocator,

    EHIR_Instruction_caps,
    EHIR_Instruction_caph,
)

from .inner.unassignable.unassignable import (
    EHIR_Unassignable_Instruction,
    EHIR_Instruction_store,
)

from .inner.unassignable.control_flow import (
    EHIR_ControlFlow,

    EHIR_Instruction_ret,
    EHIR_Instruction_br,
    EHIR_Instruction_cbr,
)

from .top.top import (
    EHIR_Instruction_imp,
    EHIR_Instruction_function_declaration,
    EHIR_Instruction_function_implementation,
    EHIR_Instruction_strucure_definition,
    EHIR_Instruction_structure_delcaration,
)

from .block import EHIR_InstructionsBlock
from .function import EHIR_FunctionDeclaration, EHIR_FunctionImplementation

__all__ = [
    "EHIR_Instruction",
    "EHIR_TopLevelInstruction",
    "EHIR_InnerInstruction",

    "EHIR_Assignable_Instruction",
    
    "EHIR_Instruction_call",
    "EHIR_Instruction_cast",
    "EHIR_Instruction_getf",
    
    "EHIR_Instruction_MemoryAllocator",
    "EHIR_Instruction_caps",
    "EHIR_Instruction_caph",
    
    "EHIR_Instruction_Binop",

    "EHIR_Instruction_add",
    "EHIR_Instruction_sub",
    "EHIR_Instruction_mul",
    "EHIR_Instruction_div",
    "EHIR_Instruction_ieq",
    "EHIR_Instruction_neq",
    "EHIR_Instruction_grt",
    "EHIR_Instruction_geq",
    "EHIR_Instruction_les",
    "EHIR_Instruction_leq",
    
    "EHIR_Unassignable_Instruction",
    
    "EHIR_Instruction_imp",
    "EHIR_Instruction_function_declaration",
    "EHIR_Instruction_function_implementation",
    "EHIR_Instruction_strucure_definition",
    "EHIR_Instruction_structure_delcaration",
    "EHIR_Instruction_store",

    "EHIR_ControlFlow",

    "EHIR_Instruction_ret",
    "EHIR_Instruction_br",
    "EHIR_Instruction_cbr",

    "EHIR_InstructionsBlock",
    "EHIR_FunctionDeclaration",
    "EHIR_FunctionImplementation",
]
