from dataclasses import dataclass
from typing import Optional

@dataclass
class EHIR_Aggregate:
    pass

@dataclass
class EHIR_StructureDeclaration(EHIR_Aggregate):
    is_public : bool
    name      : str
    
    def __repr__(self) -> str:
        return f"{'@' if self.is_public else '%'}{self.name}"

@dataclass
class EHIR_StructureDefinition(EHIR_Aggregate):
    declaration : EHIR_StructureDeclaration
    fields      : tuple["EHIR_Pointer", ...]

    def get_ith_field(self, i: int) -> Optional["EHIR_Pointer"]:
        if i < len(self.fields):
            return self.fields[i]
    
    def __repr__(self) -> str:
        res = "struct " + self.declaration.__repr__()
        res += " {\n"
        for f in self.fields:
            res += "\t" + f.__repr__() + "\n"
        res += "}"
        return res

@dataclass
class EHIR_StructureInitialization(EHIR_Aggregate):
    dynamic    : bool
    definition : EHIR_StructureDefinition
    args       : tuple["EHIR_Pointer", ...]
    
    def __repr__(self) -> str:
        return self.definition.declaration.__repr__() + " {" + ", ".join([x.__repr__() for x in self.args]) + "}"

@dataclass
class EHIR_Pointer:
    name      : str
    points_to : EHIR_StructureDeclaration

    def __repr__(self) -> str:
        return f"{self.points_to}* %{self.name}"
