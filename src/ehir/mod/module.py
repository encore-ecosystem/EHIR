from dataclasses import dataclass
from pathlib import Path
from ..instructions import (
    EHIR_Instruction_function_declaration,
    EHIR_Instruction_function_implementation,
    EHIR_Instruction_structure_delcaration,
    EHIR_Instruction_strucure_definition,
    EHIR_FunctionImplementation,
    EHIR_Instruction_caph,
    EHIR_Instruction_ret,
    EHIR_Instruction_br,
    EHIR_Instruction_cbr,
    EHIR_ControlFlow,
)
from .header import EHIR_Header
from collections import deque

@dataclass
class EHIR_Module:
    name   : str
    path   : Path
    header : EHIR_Header
    
    structure_decls : dict[str, EHIR_Instruction_structure_delcaration]
    structure_defs  : dict[str, EHIR_Instruction_strucure_definition]
    function_decls  : dict[str, EHIR_Instruction_function_declaration]
    function_defs   : dict[str, EHIR_Instruction_function_implementation]

    @property
    def is_resolved(self) -> bool:
        return len(self.header.imports) == 0

    def dump(self) -> str:
        result = ""
        
        sections = (
            ("$imports"     , self.header.imports),
            ("$struct_decls", list(self.header.structure_decls.values()) + list(self.structure_decls.values())),
            ("$struct_defs" , list(self.header.structure_defs.values()) + list(self.structure_defs.values())),
            ("$func_decl"   , list(self.header.function_decls.values()) + list(self.function_decls.values())),
            ("$func_defs"   , list(self.function_defs.values())),
        )
        
        for (section, instructions) in sections:
            result += section + "\n" * 2
            for instruction in instructions:
                result += instruction.__str__() + "\n" * 2
        
        return result
    
    def resolve(self):
        for func_name, func_def_instruction in self.function_defs.items():
            function = func_def_instruction.implementation
            self._terminate_pass(function)
            self._allocation_pass(function)
    
    def _terminate_pass(self, function: EHIR_FunctionImplementation):
        if "entry" not in function.body:
            err = f"Function {function.declaration.name} should contains `entry` block"
            raise RuntimeError(err)
        
        visited = set()
        to_visit = deque(function.body.keys())
        while to_visit:
            block_name = to_visit.popleft()
            block = function.body[block_name]
            block.terminate()

            if not block.is_end_terminated():
                err = f"Block {block_name} in function {function.declaration.name} is not end-terminated"
                raise RuntimeError(err)

            visited.add(block_name)
            
            terminator = block.body[-1]
            assert isinstance(terminator, EHIR_ControlFlow), "Compiler error"
            
            if isinstance(terminator, EHIR_Instruction_br):
                assert isinstance(terminator, EHIR_Instruction_br)
                if terminator.destination not in visited:
                    to_visit.append(terminator.destination)

            if isinstance(terminator, EHIR_Instruction_cbr):
                assert isinstance(terminator, EHIR_Instruction_cbr)
                if terminator.else_br not in visited:
                    to_visit.append(terminator.else_br)
                if terminator.true_br not in visited:
                    to_visit.append(terminator.true_br)

    def _allocation_pass(self, function: EHIR_FunctionImplementation):
        if "allocations" in function.body:
            err = f"Function {function.declaration.name}. Raw EHIR shouldn't contain `allocations` block"
            raise RuntimeError(err)
        

        visited = set()
        to_visit = deque(function.body.keys())
        while to_visit:
            block_name = to_visit.popleft()
            block = function.body[block_name]

            filtered_instructions = []
            while block.body:
                instruction = block.body.pop(0)
                if isinstance(instruction, EHIR_Instruction_caph):
                    function.allocations.append(instruction)
                else:
                    filtered_instructions.append(instruction)
            block.body = filtered_instructions
            
            visited.add(block_name)
            
            terminator = block.body[-1]
            assert isinstance(terminator, EHIR_ControlFlow), "Compiler error"
            
            if isinstance(terminator, EHIR_Instruction_br):
                assert isinstance(terminator, EHIR_Instruction_br)
                if terminator.destination not in visited:
                    to_visit.append(terminator.destination)

            if isinstance(terminator, EHIR_Instruction_cbr):
                assert isinstance(terminator, EHIR_Instruction_cbr)
                if terminator.else_br not in visited:
                    to_visit.append(terminator.else_br)
                if terminator.true_br not in visited:
                    to_visit.append(terminator.true_br)
    
    def set_resolved(self):
        assert len(self.header.imports) == 0


__all__ = [
    "EHIR_Module",
]
