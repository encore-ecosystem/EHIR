from dataclasses import dataclass

@dataclass
class EHIR_Instruction:
    pass

@dataclass
class EHIR_TopLevelInstruction(EHIR_Instruction):
    pass

@dataclass
class EHIR_InnerInstruction(EHIR_Instruction):
    pass
