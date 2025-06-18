from ..instruction import EHIR_TopLevelInstruction
from ..function import EHIR_FunctionDeclaration, EHIR_FunctionImplementation
from dataclasses import dataclass
from ...aggregate import EHIR_StructureDeclaration, EHIR_StructureDefinition

@dataclass
class EHIR_Instruction_imp(EHIR_TopLevelInstruction):  # noqa: N801
    module_name : str
    symbol      : str
    
    def __repr__(self) -> str:
        return f"imp {self.module_name}->{self.symbol}"

@dataclass
class EHIR_Instruction_function_declaration(EHIR_TopLevelInstruction):  # noqa: N801
    declaration : EHIR_FunctionDeclaration
    
    def __repr__(self) -> str:
        return self.declaration.__repr__()

@dataclass
class EHIR_Instruction_function_implementation(EHIR_TopLevelInstruction):  # noqa: N801
    implementation : EHIR_FunctionImplementation

    def __repr__(self) -> str:
        return self.implementation.__repr__()

@dataclass
class EHIR_Instruction_structure_delcaration(EHIR_TopLevelInstruction):
    declaration : EHIR_StructureDeclaration
    
    def __repr__(self) -> str:
        return self.declaration.__repr__()

@dataclass
class EHIR_Instruction_strucure_definition(EHIR_TopLevelInstruction):  # noqa: N801
    definition : EHIR_StructureDefinition

    def __repr__(self) -> str:
        return self.definition.__repr__()
