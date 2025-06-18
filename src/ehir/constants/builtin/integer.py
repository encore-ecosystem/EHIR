from ..constant import EHIR_Constant


class EHIR_IntegerConstant(EHIR_Constant):
    def __init__(self, size: int):
        self.size = size
    
    @property
    def name(self) -> str:
        return f"i{self.size}"
    
    def __repr__(self) -> str:
        return self.name
