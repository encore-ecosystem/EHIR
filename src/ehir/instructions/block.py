from dataclasses import dataclass
from .instruction import EHIR_InnerInstruction
from .inner.unassignable.control_flow import EHIR_ControlFlow

@dataclass
class EHIR_InstructionsBlock:
    name : str
    body : list[EHIR_InnerInstruction]
    
    def terminate(self) -> list[EHIR_InnerInstruction]:
        dead_code = []
        life_code = []
        
        terminated = False
        while self.body:
            instruction = self.body.pop(0)
            
            if terminated:
                dead_code.append(instruction)
            else:
                life_code.append(instruction)
            
            if isinstance(instruction, EHIR_ControlFlow):
                terminated = True
        
        self.body = life_code
        return dead_code
    
    def is_terminate(self) -> bool:
        for i, instr in enumerate(self.body):
            if isinstance(instr, EHIR_ControlFlow):
                return True
        return False
    
    def is_end_terminated(self) -> bool:
        return len(self.body) > 0 and isinstance(self.body[-1], EHIR_ControlFlow)

